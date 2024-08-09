import unittest
import asyncio
import os
from app.core.services.business_onboarding import onboard_business

class TestBusinessOnboarding(unittest.TestCase):
    def setUp(self):
        self.business_description = self.load_business_description()

    def load_business_description(self):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        description_file = os.path.join(test_dir, 'test_business_description.md')
        with open(description_file, 'r') as file:
            return file.read()

    def test_onboarding_process(self):
        ontology = asyncio.run(onboard_business(self.business_description))
        self.assertIsNotNone(ontology)
        self.assertTrue(len(ontology.concepts) > 0)
        self.assertTrue(len(ontology.relationships) > 0)

        # Add more specific assertions based on the expected ontology structure
        # For example:
        # self.assertIn('Product', ontology.concepts)
        # self.assertIn('Customer', ontology.concepts)
        # self.assertIn('has_ordered', ontology.relationships)

if __name__ == '__main__':
    unittest.main()