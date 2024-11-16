import unittest
from unittest.mock import Mock, patch
from src.db.database_manager import DatabaseManager

class TestDatabaseManager(unittest.TestCase):
    @patch('src.db.database_manager.ArangoClient')
    def setUp(self, mock_arango_client):
        self.mock_client = Mock()
        self.mock_db = Mock()
        mock_arango_client.return_value.db.return_value = self.mock_client
        self.mock_client.database.return_value = self.mock_db
        self.db_manager = DatabaseManager()

    def test_create_collection(self):
        self.mock_db.has_collection.return_value = False
        self.db_manager.create_collection("test_collection")
        self.mock_db.create_collection.assert_called_once_with("test_collection")

    def test_create_existing_collection(self):
        self.mock_db.has_collection.return_value = True
        self.db_manager.create_collection("test_collection")
        self.mock_db.create_collection.assert_not_called()

    def test_insert_document(self):
        mock_collection = Mock()
        self.mock_db.collection.return_value = mock_collection
        mock_collection.insert.return_value = {"_key": "test_key"}

        document = {"name": "Test Document"}
        result = self.db_manager.insert_document("test_collection", document)

        mock_collection.insert.assert_called_once_with(document)
        self.assertEqual(result, "test_key")

    def test_get_document(self):
        mock_collection = Mock()
        self.mock_db.collection.return_value = mock_collection
        mock_collection.get.return_value = {"_key": "test_key", "name": "Test Document"}

        result = self.db_manager.get_document("test_collection", "test_key")

        mock_collection.get.assert_called_once_with("test_key")
        self.assertEqual(result, {"_key": "test_key", "name": "Test Document"})

    def test_update_document(self):
        mock_collection = Mock()
        self.mock_db.collection.return_value = mock_collection
        mock_collection.update.return_value = {"_key": "test_key"}

        update_data = {"name": "Updated Test Document"}
        result = self.db_manager.update_document("test_collection", "test_key", update_data)

        mock_collection.update.assert_called_once_with({"_key": "test_key", **update_data})
        self.assertTrue(result)

    def test_delete_document(self):
        mock_collection = Mock()
        self.mock_db.collection.return_value = mock_collection
        mock_collection.delete.return_value = {"_key": "test_key"}

        result = self.db_manager.delete_document("test_collection", "test_key")

        mock_collection.delete.assert_called_once_with({"_key": "test_key"})
        self.assertTrue(result)

    def test_query(self):
        mock_cursor = Mock()
        self.mock_db.aql.execute.return_value = mock_cursor
        mock_cursor.__iter__.return_value = [{"name": "Test Document"}]

        aql_query = "FOR doc IN test_collection RETURN doc"
        result = self.db_manager.query(aql_query)

        self.mock_db.aql.execute.assert_called_once_with(aql_query, bind_vars=None)
        self.assertEqual(result, [{"name": "Test Document"}])

if __name__ == '__main__':
    unittest.main()