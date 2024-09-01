import csv
import os
import unittest
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.core.agents.ui_agents.onboarding_agent import OnboardingAgent
from app.core.models.knowledge.ontology.ontology import Ontology
from app.core.models.knowledge.ontology.ontology_generator import \
    OntologyGenerator
from app.core.services.erp_service import ERPService
from app.core.services.llm_service import LLMService
from app.core.services.mabos_service import MABOSService
from app.core.tools.llm_manager import LLMManager
from app.db.arango_db_client import ArangoDBClient
from app.config.config import CONFIG


class TestEcommerceOnboarding(unittest.TestCase):

    @pytest.fixture(autouse=True)
    async def setup(self):
        # Mock dependencies
        self.llm_manager = AsyncMock(spec=LLMManager)
        self.llm_service = AsyncMock(spec=LLMService)
        self.db_client = AsyncMock(spec=ArangoDBClient)
        self.erp_service = AsyncMock(spec=ERPService)
        self.mabos_service = AsyncMock(spec=MABOSService)

        # Update paths in CONFIG
        CONFIG.BUSINESS_DESCRIPTION_PATH = "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/data/business_description.md"
        CONFIG.NAICS_CODES_PATH = "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/data/2022-NAICS-Codes-listed-numerically-2-Digit-through-6-Digit.csv"

        # Create OnboardingAgent instance
        self.onboarding_agent = await OnboardingAgent.create(
            llm_agent=AsyncMock(),
            db_client=self.db_client,
            erp_service=self.erp_service,
            mabos_service=self.mabos_service
        )

        # Create OntologyGenerator instance
        self.ontology_generator = OntologyGenerator(
            llm_manager=self.llm_manager,
            llm_service=self.llm_service
        )

        # Load sample business description
        with open(CONFIG.BUSINESS_DESCRIPTION_PATH, 'r') as file:
            self.business_description = file.read()

    @pytest.mark.asyncio
    async def test_load_example_business(self):
        result = await self.onboarding_agent._load_example_business()
        self.assertIsInstance(result, dict)
        self.assertIn('business_description', result)
        self.assertGreater(len(result['business_description']), 0)

    @pytest.mark.asyncio
    async def test_conduct_onboarding_with_example(self):
        with patch('app.db.togaf_questions.create_database_and_collections') as mock_create_db, \
             patch('app.db.togaf_questions.seed_questions') as mock_seed_questions:
            
            mock_db = MagicMock()
            mock_create_db.return_value = mock_db

            result = await self.onboarding_agent.conduct_onboarding(use_example=True)
            
            # Assert that database creation and seeding were called
            mock_create_db.assert_called_once()
            mock_seed_questions.assert_called_once_with(mock_db)

            self.assertIsInstance(result, dict)
            self.assertIn('business_description', result)
            self.assertGreater(len(result['business_description']), 0)

    @pytest.mark.asyncio
    async def test_generate_ontology(self):
        # Mock the generate_ontology method
        self.ontology_generator.generate_ontology = AsyncMock(return_value=Ontology(
            concepts=["Product", "Customer", "Order", "ShoppingCart"],
            relationships=[
                {"name": "places", "source": "Customer", "target": "Order"},
                {"name": "contains", "source": "ShoppingCart", "target": "Product"}
            ]
        ))

        ontology = await self.ontology_generator.generate_ontology(self.business_description)

        self.assertIn("Product", ontology.concepts)
        self.assertIn("Customer", ontology.concepts)
        self.assertIn("Order", ontology.concepts)
        self.assertIn("ShoppingCart", ontology.concepts)

        self.assertTrue(any(r.name == "places" and r.source == "Customer" and r.target == "Order" for r in ontology.relationships))
        self.assertTrue(any(r.name == "contains" and r.source == "ShoppingCart" and r.target == "Product" for r in ontology.relationships))

    @pytest.mark.asyncio
    async def test_create_mabos_agent(self):
        initial_config = {"agent_name": "EcommerceAgent"}
        business_domain_ontology = {"concepts": ["Product", "Customer", "Order"]}

        self.onboarding_agent.create_mabos_agent = AsyncMock(return_value={"agent_id": "mabos-123"})

        result = await self.onboarding_agent.create_mabos_agent(initial_config, business_domain_ontology)

        self.assertEqual(result["agent_id"], "mabos-123")

    @pytest.mark.asyncio
    async def test_load_naics_codes(self):
        naics_codes = self.onboarding_agent.naics_codes

        self.assertIsInstance(naics_codes, dict)
        self.assertGreater(len(naics_codes), 0)
        self.assertIn("Electronics Stores", naics_codes)
        self.assertEqual(naics_codes["Electronics Stores"], "443142")

    @pytest.mark.asyncio
    async def test_collect_business_information(self):
        # Mock the _ask_question method
        self.onboarding_agent._ask_question = AsyncMock(side_effect=[
            "TechElectronics",
            "Electronics Retail",
            "Medium"
        ])

        business_data = {}
        await self.onboarding_agent._collect_business_information(business_data)

        self.assertEqual(business_data["your_business_name"], "TechElectronics")
        self.assertEqual(business_data["your_business_industry"], "Electronics Retail")
        self.assertEqual(business_data["your_business_size"], "Medium")
        self.assertEqual(business_data["naics_code"], "443142")

    @pytest.mark.asyncio
    async def test_manual_togaf_questions(self):
        # Mock the _ask_question method to simulate user input
        self.onboarding_agent._ask_question = AsyncMock(side_effect=[
            "TechElectronics",
            "Electronics Retail",
            "Medium",
            "We sell high-quality electronics online",
            "Increase market share by 10%",
            "Improve customer satisfaction",
            "Expand product range",
            "Enhance online shopping experience",
            "Implement AI-powered recommendations"
        ])

        # Mock the LLMAgent's generate_business_description method
        self.onboarding_agent.llm_agent.generate_business_description = AsyncMock(
            return_value="TechElectronics is a medium-sized electronics retail business..."
        )

        # Mock the _generate_ontology method
        self.onboarding_agent._generate_ontology = AsyncMock(
            return_value={"concepts": ["Product", "Customer", "Order"], "relationships": []}
        )

        # Call the conduct_onboarding method with manual input
        result = await self.onboarding_agent.conduct_onboarding(use_example=False)

        # Assert the result
        self.assertIn("your_business_name", result)
        self.assertIn("your_business_industry", result)
        self.assertIn("your_business_size", result)
        self.assertIn("business_description", result)
        self.assertIn("ontology", result)

        # Check if the business description was generated using LLM
        self.assertTrue(self.onboarding_agent.llm_agent.generate_business_description.called)

        # Check if the ontology was generated
        self.assertTrue(self.onboarding_agent._generate_ontology.called)

    @pytest.mark.asyncio
    async def test_ask_togaf_questions(self):
        # Mock the get_all_questions function
        with patch('app.db.togaf_questions.get_all_questions', new_callable=AsyncMock) as mock_get_questions:
            mock_get_questions.return_value = {
                "general_information": ["What is your organization's name?"],
                "business_architecture": ["What are your key business functions?"]
            }

            # Mock the _ask_question method
            self.onboarding_agent._ask_question = AsyncMock(side_effect=[
                "TechElectronics",
                "Sales, Customer Service, Inventory Management"
            ])

            business_data = {}
            await self.onboarding_agent._ask_togaf_questions(business_data)

            self.assertIn("general_information", business_data)
            self.assertIn("business_architecture", business_data)
            self.assertEqual(business_data["general_information"]["What is your organization's name?"], "TechElectronics")
            self.assertEqual(business_data["business_architecture"]["What are your key business functions?"], "Sales, Customer Service, Inventory Management")

if __name__ == '__main__':
    unittest.main()