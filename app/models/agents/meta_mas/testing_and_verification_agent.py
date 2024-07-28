from datetime import time
from typing import List, Dict, Any
import psutil

from pynusmv.src.pynusmv import mc
from meta_agents import MetaAgent
import pynusmv
from pynusmv.src.pynusmv.init import init_nusmv, deinit_nusmv
from pynusmv.src.pynusmv.glob import load, prop_database

with pynusmv.init.init_nusmv():
       pynusmv.glob.load_from_file("counters.smv")
       pynusmv.glob.compute_model()
       fsm = pynusmv.glob.prop_database().master.bddFsm
       prop = pynusmv.glob.prop_database()[0]
       spec = prop.expr
       bdd = pynusmv.mc.eval_ctl_spec(fsm, spec) & fsm.reachable_states
       satstates = fsm.pick_all_states(bdd)
       for state in satstates:
           print(state.get_str_values())

class TestingAndVerificationAgent(MetaAgent):
    """
    Ensures the quality and correctness of the generated domain-specific MAS.
    
    Key functions:
    - Develop and execute test cases
    - Perform model checking and formal verification
    - Validate agent behaviors against requirements
    - Conduct performance testing and optimization
    """
    def develop_test_cases(self, requirements: Dict[str, Any], agent_designs: Dict[str, Any]) -> Dict[str, Any]:
        test_cases = {}
        
        for req_id, requirement in requirements.items():
            test_cases[req_id] = []
            
            # Functional requirements
            if 'functionality' in requirement:
                test_cases[req_id].append({
                    'type': 'functional',
                    'description': f"Test {requirement['functionality']}",
                    'expected_result': requirement.get('expected_outcome', 'Successful execution of functionality')
                })
            
            # Performance requirements
            if 'performance' in requirement:
                test_cases[req_id].append({
                    'type': 'performance',
                    'description': f"Measure performance of {requirement['performance']}",
                    'expected_result': f"Performance meets or exceeds {requirement.get('performance_target', 'specified target')}"
                })
            
            # Security requirements
            if 'security' in requirement:
                test_cases[req_id].append({
                    'type': 'security',
                    'description': f"Verify security measure: {requirement['security']}",
                    'expected_result': 'No security vulnerabilities detected'
                })
        
        # Agent-specific test cases
        for agent_id, design in agent_designs.items():
            test_cases[f"agent_{agent_id}"] = []
            
            # Test agent initialization
            test_cases[f"agent_{agent_id}"].append({
                'type': 'initialization',
                'description': f"Initialize agent {agent_id}",
                'expected_result': 'Agent successfully initialized with correct parameters'
            })
            
            # Test agent behaviors
            for behavior in design.get('behaviors', []):
                test_cases[f"agent_{agent_id}"].append({
                    'type': 'behavior',
                    'description': f"Test behavior: {behavior}",
                    'expected_result': 'Behavior executes correctly and produces expected output'
                })
            
            # Test agent interactions
            for interaction in design.get('interactions', []):
                test_cases[f"agent_{agent_id}"].append({
                    'type': 'interaction',
                    'description': f"Test interaction: {interaction}",
                    'expected_result': 'Interaction occurs successfully with correct data exchange'
                })
        
        return test_cases
    
    def execute_test_cases(self, test_cases: Dict[str, Any], mas_implementation: Dict[str, Any]) -> Dict[str, Any]:
        results = {}
        for test_id, test_list in test_cases.items():
            results[test_id] = []
            for test in test_list:
                test_result = {
                    'type': test['type'],
                    'description': test['description'],
                    'expected_result': test['expected_result'],
                    'actual_result': None,
                    'status': 'FAILED'
                }
                
                try:
                    if test['type'] == 'functional':
                        actual_result = self._execute_functional_test(test, mas_implementation)
                    elif test['type'] == 'performance':
                        actual_result = self._execute_performance_test(test, mas_implementation)
                    elif test['type'] == 'security':
                        actual_result = self._execute_security_test(test, mas_implementation)
                    elif test['type'] == 'initialization':
                        actual_result = self._execute_initialization_test(test, mas_implementation)
                    elif test['type'] == 'behavior':
                        actual_result = self._execute_behavior_test(test, mas_implementation)
                    elif test['type'] == 'interaction':
                        actual_result = self._execute_interaction_test(test, mas_implementation)
                    else:
                        actual_result = f"Unknown test type: {test['type']}"
                    
                    test_result['actual_result'] = actual_result
                    if self._compare_results(actual_result, test['expected_result']):
                        test_result['status'] = 'PASSED'
                
                except Exception as e:
                    test_result['actual_result'] = f"Error: {str(e)}"
                
                results[test_id].append(test_result)
        
        return results

    def _execute_functional_test(self, test: Dict[str, Any], mas_implementation: Dict[str, Any]) -> str:
        # Implement functional test execution logic
        agent_id = test.get('agent_id')
        function_name = test.get('function_name')
        input_data = test.get('input_data', {})
        expected_output = test.get('expected_output')

        if not agent_id or not function_name:
            return "Error: Missing agent_id or function_name in test specification"

        agent = mas_implementation.get(agent_id)
        if not agent:
            return f"Error: Agent {agent_id} not found in MAS implementation"

        try:
            function = getattr(agent, function_name)
            actual_output = function(**input_data)
            
            if actual_output == expected_output:
                return f"Functional test passed: {function_name} returned expected output"
            else:
                return f"Functional test failed: {function_name} returned {actual_output}, expected {expected_output}"
        except AttributeError:
            return f"Error: Function {function_name} not found in agent {agent_id}"
        except Exception as e:
            return f"Error executing functional test: {str(e)}"

    def _execute_performance_test(self, test: Dict[str, Any], mas_implementation: Dict[str, Any]) -> str:
        # Implement performance test execution logic
        import time
        
        agent_id = test.get('agent_id')
        function_name = test.get('function_name')
        input_data = test.get('input_data', {})
        expected_time = test.get('expected_time')
        
        if not agent_id or not function_name or expected_time is None:
            return "Error: Missing required test parameters"
        
        agent = mas_implementation.get(agent_id)
        if not agent:
            return f"Error: Agent {agent_id} not found in MAS implementation"
        
        try:
            function = getattr(agent, function_name)
            
            start_time = time.time()
            function(**input_data)
            end_time = time.time()
            
            execution_time = end_time - start_time
            
            if execution_time <= expected_time:
                return f"Performance test passed: {function_name} executed in {execution_time:.4f} seconds (expected <= {expected_time} seconds)"
            else:
                return f"Performance test failed: {function_name} executed in {execution_time:.4f} seconds (expected <= {expected_time} seconds)"
        except AttributeError:
            return f"Error: Function {function_name} not found in agent {agent_id}"
        except Exception as e:
            return f"Error executing performance test: {str(e)}"

    def _execute_security_test(self, test: Dict[str, Any], mas_implementation: Dict[str, Any]) -> str:
        agent_id = test.get('agent_id')
        function_name = test.get('function_name')
        input_data = test.get('input_data', {})
        expected_result = test.get('expected_result')
        
        if not agent_id or not function_name or not expected_result:
            return "Error: Missing required test parameters"
        
        agent = mas_implementation.get(agent_id)
        if not agent:
            return f"Error: Agent {agent_id} not found in MAS implementation"
        
        try:
            function = getattr(agent, function_name)
            
            # Simulate potential security threats
            malicious_input = self._generate_malicious_input(input_data)
            
            # Execute the function with malicious input
            actual_result = function(**malicious_input)
            
            # Check if the function handled the malicious input correctly
            if self._compare_results(str(actual_result), expected_result):
                return f"Security test passed: {function_name} handled malicious input correctly"
            else:
                return f"Security test failed: {function_name} did not handle malicious input as expected"
        except AttributeError:
            return f"Error: Function {function_name} not found in agent {agent_id}"
        except Exception as e:
            return f"Security vulnerability detected: {str(e)}"

    def _generate_malicious_input(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        # Generate malicious input based on the original input
        malicious_input = input_data.copy()
        for key, value in malicious_input.items():
            if isinstance(value, str):
                malicious_input[key] = value + "'; DROP TABLE users; --"
            elif isinstance(value, int):
                malicious_input[key] = 9999999999
        return malicious_input

    def _execute_initialization_test(self, test: Dict[str, Any], mas_implementation: Dict[str, Any]) -> str:
        agent_id = test.get('agent_id')
        expected_attributes = test.get('expected_attributes', {})
        
        if not agent_id or not expected_attributes:
            return "Error: Missing required test parameters"
        
        agent = mas_implementation.get(agent_id)
        if not agent:
            return f"Error: Agent {agent_id} not found in MAS implementation"
        
        initialization_errors = []
        for attr, expected_value in expected_attributes.items():
            if not hasattr(agent, attr):
                initialization_errors.append(f"Attribute '{attr}' not found in agent {agent_id}")
            elif getattr(agent, attr) != expected_value:
                actual_value = getattr(agent, attr)
                initialization_errors.append(f"Attribute '{attr}' has value '{actual_value}', expected '{expected_value}'")
        
        if initialization_errors:
            return f"Initialization test failed: {'; '.join(initialization_errors)}"
        else:
            return f"Initialization test passed: All expected attributes correctly initialized for agent {agent_id}"

    def _execute_behavior_test(self, test: Dict[str, Any], mas_implementation: Dict[str, Any]) -> str:
        # Implement behavior test execution logic
        return "Behavior test executed"

    def _execute_interaction_test(self, test: Dict[str, Any], mas_implementation: Dict[str, Any]) -> str:
        agent_id = test.get('agent_id')
        interaction_type = test.get('interaction_type')
        target_agent_id = test.get('target_agent_id')
        interaction_params = test.get('interaction_params', {})
        expected_result = test.get('expected_result')

        if not all([agent_id, interaction_type, target_agent_id, expected_result]):
            return "Error: Missing required test parameters"

        agent = mas_implementation.get(agent_id)
        target_agent = mas_implementation.get(target_agent_id)

        if not agent or not target_agent:
            return f"Error: One or both agents not found in MAS implementation"

        try:
            interaction_method = getattr(agent, interaction_type)
            actual_result = interaction_method(target_agent, **interaction_params)

            if self._compare_results(str(actual_result), expected_result):
                return f"Interaction test passed: {agent_id} successfully interacted with {target_agent_id}"
            else:
                return f"Interaction test failed: Unexpected result from {interaction_type} interaction"
        except AttributeError:
            return f"Error: Interaction method {interaction_type} not found in agent {agent_id}"
        except Exception as e:
            return f"Interaction test failed: {str(e)}"

    def _compare_results(self, actual_result: str, expected_result: str) -> bool:
        # Implement result comparison logic
        actual_result = actual_result.strip().lower()
        expected_result = expected_result.strip().lower()

        # Exact match
        if actual_result == expected_result:
            return True

        # Check if the actual result contains the expected result
        if expected_result in actual_result:
            return True

        # Check for semantic similarity using a threshold
        similarity_threshold = 0.8
        similarity = self._calculate_semantic_similarity(actual_result, expected_result)
        if similarity >= similarity_threshold:
            return True

        return False

    def _calculate_semantic_similarity(self, text1: str, text2: str) -> float:
        # This method should be implemented using a suitable NLP library
        # For now, we'll use a simple placeholder implementation
        common_words = set(text1.split()) & set(text2.split())
        total_words = set(text1.split()) | set(text2.split())
        return len(common_words) / len(total_words)
    
    def perform_model_checking(self, agent_models: Dict[str, Any]) -> bool:
        """
        Perform model checking and formal verification on agent models.

        Args:
            agent_models (Dict[str, Any]): A dictionary of agent models to be verified.

        Returns:
            bool: True if all models pass verification, False otherwise.
        """

        init_nusmv()
        try:
            for agent_id, model in agent_models.items():
                # Load the agent model
                load(model)

                # Get all CTL properties defined in the model
                props = prop_database().get_ctl_properties()

                # Check each property
                for prop in props:
                    spec = prop.get_expr()
                    is_valid = mc.check_ctl_spec(spec)
                    if not is_valid:
                        print(f"Property {prop.get_name()} does not hold for agent {agent_id}")
                        return False

                # Check for deadlocks
                if mc.check_deadlock():
                    print(f"Deadlock detected in agent model {agent_id}")
                    return False

            return True
        finally:
            deinit_nusmv()
    
    def validate_agent_behaviors(self, agent_implementations: Dict[str, Any], requirements: Dict[str, Any]) -> bool:
        """
        Validate agent behaviors against requirements.

        Args:
            agent_implementations (Dict[str, Any]): A dictionary of agent implementations.
            requirements (Dict[str, Any]): A dictionary of requirements.

        Returns:
            bool: True if all agent behaviors meet the requirements, False otherwise.
        """
        for agent_id, implementation in agent_implementations.items():
            agent_requirements = requirements.get(agent_id, {})
            for req_id, requirement in agent_requirements.items():
                if not self._validate_single_requirement(implementation, requirement):
                    print(f"Agent {agent_id} failed to meet requirement {req_id}")
                    return False
        
        return True

    def _validate_single_requirement(self, implementation: Any, requirement: Dict[str, Any]) -> bool:
        # This method should be implemented based on the specific structure of
        # implementations and requirements. Here's a simple example:
        if 'behavior' in requirement:
            expected_behavior = requirement['behavior']
            actual_behavior = self._extract_behavior(implementation)
            return self._compare_behaviors(actual_behavior, expected_behavior)
        return True

    def _extract_behavior(self, implementation: Any) -> str:
        # Extract behavior from implementation
        # This is a placeholder and should be implemented based on the actual structure of the implementation
        return str(implementation)

    def _compare_behaviors(self, actual_behavior: str, expected_behavior: str) -> bool:
        # Compare actual behavior with expected behavior
        # This could use natural language processing techniques for more sophisticated comparison
        return self._calculate_semantic_similarity(actual_behavior, expected_behavior) > 0.8
    
    def conduct_performance_testing(self, mas_implementation: Dict[str, Any]) -> Dict[str, Any]:
        performance_results = {}
        
        for agent_id, agent_impl in mas_implementation.items():
            # Measure execution time
            start_time = time.time()
            agent_impl.run_simulation(iterations=1000)  # Adjust iterations as needed
            end_time = time.time()
            execution_time = end_time - start_time
            
            # Measure memory usage
            memory_usage = psutil.Process().memory_info().rss / (1024 * 1024)  # in MB
            
            # Measure CPU usage
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # Store results
            performance_results[agent_id] = {
                "execution_time": execution_time,
                "memory_usage": memory_usage,
                "cpu_usage": cpu_usage
            }
        
        # Identify bottlenecks and suggest optimizations
        for agent_id, metrics in performance_results.items():
            if metrics["execution_time"] > 5:  # Adjust threshold as needed
                print(f"Performance bottleneck detected in {agent_id}: High execution time")
                print("Suggestion: Optimize algorithm or use parallel processing")
            
            if metrics["memory_usage"] > 500:  # Adjust threshold as needed
                print(f"Performance bottleneck detected in {agent_id}: High memory usage")
                print("Suggestion: Implement memory-efficient data structures or use lazy loading")
            
            if metrics["cpu_usage"] > 80:  # Adjust threshold as needed
                print(f"Performance bottleneck detected in {agent_id}: High CPU usage")
                print("Suggestion: Optimize computationally intensive tasks or distribute workload")
        
        return performance_results
