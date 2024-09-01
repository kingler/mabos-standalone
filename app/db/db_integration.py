from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel
from arango import ArangoClient
from dotenv import load_dotenv
import os
import numpy as np
from sentence_transformers import SentenceTransformer

load_dotenv()

class Answer(BaseModel):
    id: UUID
    content: str
    business_id: UUID

class Question(BaseModel):
    id: UUID
    content: str
    business_id: UUID

class SearchResult(BaseModel):
    movie: str
    cos_sim: float

class DatabaseIntegration:
    def __init__(self):
        self.client = self._get_arango_client()
        self.db = self._get_arango_db(self.client)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def _get_arango_client(self):
        arango_url = os.getenv("ARANGO_URL", "http://localhost:8529")
        arango_username = os.getenv("ARANGO_USERNAME", "root")
        arango_password = os.getenv("ARANGO_PASSWORD", "difyai123456")
        return ArangoClient(hosts=arango_url).db(arango_username, arango_password)

    def _get_arango_db(self, client, db_name="dify"):
        if not client.has_database(db_name):
            client.create_database(db_name)
        return client.database(db_name)

    async def create_question(self, question: Question) -> Question:
        collection = self.db.collection('questions')
        result = collection.insert(question.dict())
        question.id = result['_key']
        return question

    async def create_answer(self, answer: Answer) -> Answer:
        collection = self.db.collection('answers')
        result = collection.insert(answer.dict())
        answer.id = result['_key']
        return answer

    async def get_answers_for_business(self, business_id: UUID) -> List[Answer]:
        query = f"FOR a IN answers FILTER a.business_id == '{business_id}' RETURN a"
        cursor = self.db.aql.execute(query)
        return [Answer(**doc) for doc in cursor]

    async def create_movie_embeddings(self, movies_df):
        batch_size = 32
        all_embs = []

        for i in range(0, len(movies_df), batch_size):
            descr_batch = movies_df.iloc[i:i+batch_size].description.tolist()
            embs = self.model.encode(descr_batch)
            all_embs.append(embs)

        all_embs = np.concatenate(all_embs)
        movies_df.loc[:, "word_emb"] = np.vsplit(all_embs, len(all_embs))
        movies_df["word_emb"] = movies_df["word_emb"].apply(lambda x: x.squeeze().tolist())

        movie_collection = self.db.collection("imdb_vertices")
        for i in range(0, len(movies_df), batch_size):
            update_batch = movies_df.loc[i:i+batch_size, ["_id", "word_emb"]].to_dict("records")
            movie_collection.import_bulk(update_batch, on_duplicate="update")

    async def search_similar_movies(self, movie_id: str, limit: int = 50) -> List[SearchResult]:
        query = f"""
        LET descr_emb = (
          FOR m in imdb_vertices
            FILTER m._id == "{movie_id}"
            FOR j in RANGE(0, 767)
              RETURN TO_NUMBER(NTH(m.word_emb,j))
        )

        LET descr_mag = (
          SQRT(SUM(
            FOR i IN RANGE(0, 767)
              RETURN POW(TO_NUMBER(NTH(descr_emb, i)), 2)
          ))
        )

        LET dau = (
            FOR v in imdb_vertices
            FILTER HAS(v, "word_emb")

            LET v_mag = (SQRT(SUM(
              FOR k IN RANGE(0, 767)
                RETURN POW(TO_NUMBER(NTH(v.word_emb, k)), 2)
            )))

            LET numerator = (SUM(
              FOR i in RANGE(0,767)
                  RETURN TO_NUMBER(NTH(descr_emb, i)) * TO_NUMBER(NTH(v.word_emb, i))
            ))

            LET cos_sim = (numerator)/(descr_mag * v_mag)

            RETURN {{"movie": v.title, "cos_sim": cos_sim}}
        )

        FOR du in dau
            SORT du.cos_sim DESC
            LIMIT {limit}
            RETURN du
        """
        cursor = self.db.aql.execute(query)
        return [SearchResult(**doc) for doc in cursor]

    async def search_movies_by_query(self, search_term: str, limit: int = 50) -> List[SearchResult]:
        search_emb = self.model.encode(search_term).tolist()
        query = f"""
        LET descr_emb = {search_emb}

        LET descr_size = (
          SQRT(SUM(
            FOR i IN RANGE(0, 767)
              RETURN POW(TO_NUMBER(NTH(descr_emb, i)), 2)
          ))
        )

        LET dau = (
            FOR v in imdb_vertices
            FILTER HAS(v, "word_emb")

            LET v_size = (SQRT(SUM(
              FOR k IN RANGE(0, 767)
                RETURN POW(TO_NUMBER(NTH(v.word_emb, k)), 2)
            )))

            LET numerator = (SUM(
              FOR i in RANGE(0,767)
                  RETURN TO_NUMBER(NTH(descr_emb, i)) * TO_NUMBER(NTH(v.word_emb, i))
            ))

            LET cos_sim = (numerator)/(descr_size * v_size)

            RETURN {{"movie": v.title, "cos_sim": cos_sim}}
        )

        FOR du in dau
            SORT du.cos_sim DESC
            LIMIT {limit}
            RETURN du
        """
        cursor = self.db.aql.execute(query)
        return [SearchResult(**doc) for doc in cursor]

# Usage example:
# db = DatabaseIntegration()
# similar_movies = await db.search_similar_movies("imdb_vertices/28685")
# query_results = await db.search_movies_by_query("jedi stars fighting")