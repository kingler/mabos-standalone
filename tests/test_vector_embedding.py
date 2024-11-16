import unittest
from unittest.mock import Mock, patch
import numpy as np
from src.search.vector_embedding import VectorEmbedding

class TestVectorEmbedding(unittest.TestCase):
    @patch('src.search.vector_embedding.SentenceTransformer')
    @patch('src.search.vector_embedding.DatabaseManager')
    def setUp(self, mock_db_manager, mock_sentence_transformer):
        self.mock_model = mock_sentence_transformer.return_value
        self.mock_db = mock_db_manager.return_value
        self.vec_embed = VectorEmbedding()

    def test_encode(self):
        texts = ["This is a test", "Another test sentence"]
        expected_output = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
        self.mock_model.encode.return_value = expected_output

        result = self.vec_embed.encode(texts)

        self.mock_model.encode.assert_called_once_with(texts)
        np.testing.assert_array_equal(result, expected_output)

    def test_create_embeddings(self):
        collection_name = "test_collection"
        text_field = "description"
        documents = [
            {"_key": "1", "description": "First document"},
            {"_key": "2", "description": "Second document"}
        ]
        self.mock_db.query.return_value = documents

        embeddings = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
        self.mock_model.encode.return_value = embeddings

        self.vec_embed.create_embeddings(collection_name, text_field)

        self.mock_db.query.assert_called_once_with(f"FOR doc IN {collection_name} RETURN doc")
        self.mock_model.encode.assert_called_once_with(["First document", "Second document"])
        self.mock_db.update_document.assert_any_call(collection_name, "1", {'embedding': [0.1, 0.2, 0.3]})
        self.mock_db.update_document.assert_any_call(collection_name, "2", {'embedding': [0.4, 0.5, 0.6]})

    def test_search(self):
        collection_name = "test_collection"
        query = "test query"
        top_k = 3

        query_embedding = np.array([0.1, 0.2, 0.3])
        self.mock_model.encode.return_value = query_embedding

        expected_results = [
            {"document": {"_key": "1", "description": "First document"}, "similarity": 0.9},
            {"document": {"_key": "2", "description": "Second document"}, "similarity": 0.8}
        ]
        self.mock_db.query.return_value = expected_results

        results = self.vec_embed.search(collection_name, query, top_k)

        self.mock_model.encode.assert_called_once_with([query])
        self.mock_db.query.assert_called_once()
        self.assertEqual(results, expected_results)

    @patch('src.search.vector_embedding.np.array')
    def test_search_aql_query(self, mock_np_array):
        collection_name = "test_collection"
        query = "test query"
        top_k = 3

        query_embedding = [0.1, 0.2, 0.3]
        mock_np_array.return_value = query_embedding

        self.vec_embed.search(collection_name, query, top_k)

        # Check if the AQL query is correctly formatted
        called_args = self.mock_db.query.call_args[0][0]
        self.assertIn(f"FOR doc IN {collection_name}", called_args)
        self.assertIn("SORT similarity DESC", called_args)
        self.assertIn("LIMIT @top_k", called_args)

        # Check if bind variables are correctly set
        called_kwargs = self.mock_db.query.call_args[1]['bind_vars']
        self.assertEqual(called_kwargs['query_embedding'], query_embedding)
        self.assertEqual(called_kwargs['top_k'], top_k)

if __name__ == '__main__':
    unittest.main()