from typing import List, Dict, Any
from app.db.db_integration import DatabaseIntegration

class DistributedKnowledge:
    """
    A class for managing distributed knowledge across a database.
    """

    def __init__(self, db_integration: DatabaseIntegration):
        """
        Initialize the DistributedKnowledge class.

        Args:
            db_integration (DatabaseIntegration): An instance of DatabaseIntegration for database operations.
        """
        self.db_integration = db_integration

    async def store_distributed(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Store distributed knowledge in the appropriate database table.

        Args:
            data (Dict[str, Any]): The data to be stored.

        Returns:
            Dict[str, Any]: A dictionary containing the status and message of the operation.
        """
        try:
            table_name = self._determine_table(data)
            result = await self.db_integration.insert_data(table_name, data)
            
            if result:
                return {"status": "success", "message": f"Data stored successfully in {table_name}"}
            else:
                return {"status": "error", "message": "Failed to store data"}
        except Exception as e:
            return {"status": "error", "message": f"Error storing data: {str(e)}"}

    def _determine_table(self, data: Dict[str, Any]) -> str:
        """
        Determine the appropriate table based on the data structure.

        Args:
            data (Dict[str, Any]): The data to be analyzed.

        Returns:
            str: The name of the appropriate table.
        """
        if "agent_id" in data:
            return "agent_knowledge"
        elif "task_id" in data:
            return "task_knowledge"
        else:
            return "general_knowledge"

    async def retrieve_distributed(self, query: str) -> List[Dict[str, Any]]:
        """
        Retrieve distributed knowledge based on a given query.

        Args:
            query (str): The SQL query to execute.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing the query results.
        """
        try:
            results = await self.db_integration.execute_query(query)
            return [dict(row) for row in results]
        except Exception as e:
            print(f"Error retrieving distributed knowledge: {str(e)}")
            return []

    async def process_distributed(self, operation: str, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Process distributed knowledge based on the specified operation.

        Args:
            operation (str): The operation to perform ('aggregate', 'filter', or 'transform').
            data (List[Dict[str, Any]]): The data to process.

        Returns:
            Dict[str, Any]: A dictionary containing the status and result of the operation.
        """
        try:
            result = {}
            if operation == "aggregate":
                result = await self._aggregate_data(data)
            elif operation == "filter":
                result = await self._filter_data(data)
            elif operation == "transform":
                result = await self._transform_data(data)
            else:
                raise ValueError(f"Unsupported operation: {operation}")
            
            return {"status": "success", "result": result}
        except Exception as e:
            return {"status": "error", "message": f"Error processing distributed data: {str(e)}"}

    async def _aggregate_data(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Aggregate the given data.

        Args:
            data (List[Dict[str, Any]]): The data to aggregate.

        Returns:
            Dict[str, Any]: The aggregated data.
        """
        aggregated = {}
        for item in data:
            for key, value in item.items():
                if isinstance(value, (int, float)):
                    aggregated[key] = aggregated.get(key, 0) + value
                elif isinstance(value, str):
                    if key not in aggregated:
                        aggregated[key] = set()
                    aggregated[key].add(value)
        
        # Convert sets to lists for JSON serialization
        for key, value in aggregated.items():
            if isinstance(value, set):
                aggregated[key] = list(value)
        
        return aggregated

    async def _filter_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Filter the given data based on predefined criteria.

        Args:
            data (List[Dict[str, Any]]): The data to filter.

        Returns:
            List[Dict[str, Any]]: The filtered data.
        """
        return [item for item in data if self._meets_filter_criteria(item)]

    def _meets_filter_criteria(self, item: Dict[str, Any]) -> bool:
        """
        Check if an item meets the filter criteria.

        Args:
            item (Dict[str, Any]): The item to check.

        Returns:
            bool: True if the item meets the criteria, False otherwise.
        """
        # Implement filter criteria
        if 'value' not in item:
            return False
        
        if isinstance(item['value'], (int, float)):
            return item['value'] > 0
        elif isinstance(item['value'], str):
            return len(item['value']) > 0
        elif isinstance(item['value'], list):
            return len(item['value']) > 0
        elif isinstance(item['value'], dict):
            return len(item['value']) > 0
        else:
            return False

    async def _transform_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Transform the given data.

        Args:
            data (List[Dict[str, Any]]): The data to transform.

        Returns:
            List[Dict[str, Any]]: The transformed data.
        """
        return [self._transform_item(item) for item in data]

    def _transform_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transform a single item.

        Args:
            item (Dict[str, Any]): The item to transform.

        Returns:
            Dict[str, Any]: The transformed item.
        """
        transformed = item.copy()
        
        # Normalize string values
        if isinstance(transformed.get('value'), str):
            transformed['value'] = transformed['value'].strip().lower()
        
        # Convert numeric values to float
        elif isinstance(transformed.get('value'), (int, float)):
            transformed['value'] = float(transformed['value'])
        
        # Flatten nested structures
        elif isinstance(transformed.get('value'), (list, dict)):
            transformed['value'] = json.dumps(transformed['value'])
        
        # Add metadata
        transformed['processed_timestamp'] = datetime.now().isoformat()
        transformed['source'] = self.__class__.__name__
        
        # Categorize the item based on its content
        transformed['category'] = self._categorize_item(transformed)
        
        return transformed