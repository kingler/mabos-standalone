from arango import ArangoClient

class ProjectGraph:
    def __init__(self, host, port, username, password, database):
        self.client = ArangoClient(hosts=f"http://{host}:{port}")
        self.db = self.client.db(database, username=username, password=password)
    
    def add_reasoning_problem(self, problem_id, problem_type, description):
        problems = self.db.collection('ReasoningProblems')
        problems.insert({
            '_key': problem_id,
            'type': problem_type,
            'description': description
        })
    
    def add_reasoning_solution(self, problem_id, solution_id, method_used, description):
        solutions = self.db.collection('ReasoningSolutions')
        solutions.insert({
            '_key': solution_id,
            'problem_id': problem_id,
            'method': method_used,
            'description': description
        })
    
    def query_reasoning_effectiveness(self, problem_type):
        aql = """
        FOR p IN ReasoningProblems
        FILTER p.type == @type
        FOR s IN ReasoningSolutions
        FILTER s.problem_id == p._key
        COLLECT method = s.method
        AGGREGATE usage = COUNT(s), avg_effectiveness = AVG(s.effectiveness)
        SORT avg_effectiveness DESC
        RETURN { method, usage, avg_effectiveness }
        """
        return self.db.aql.execute(aql, bind_vars={'type': problem_type})