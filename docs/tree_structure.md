mabos-standalone/
├── __init__.py
├── README.md
├── app
│   ├── api
│   │   ├── __init__.py
│   │   └── routes
│   │       ├── __init__.py
│   │       ├── actions.py
│   │       ├── agent_roles.py
│   │       ├── agents.py
│   │       ├── archimate_service.py
│   │       ├── beliefs.py
│   │       ├── business_models.py
│   │       ├── business_plan.py
│   │       ├── communication.py
│   │       ├── desires.py
│   │       ├── environment.py
│   │       ├── erp.py
│   │       ├── erp_router.py
│   │       ├── goals.py
│   │       ├── intentions.py
│   │       ├── knowledge_bases.py
│   │       ├── mabos_routers.py
│   │       ├── mas.py
│   │       ├── mas_modeling.py
│   │       ├── mas_router.py
│   │       ├── mdd_mas.py
│   │       ├── ontology.py
│   │       ├── organization.py
│   │       ├── planning.py
│   │       ├── plans.py
│   │       ├── question.py
│   │       ├── question_router.py
│   │       ├── repository.py
│   │       ├── rules_engine.py
│   │       ├── tasks.py
│   │       ├── togaf_mdd.py
│   │       ├── topic_map.py
│   │       ├── tropos_mdd.py
│   │       ├── version_control.py
│   │       ├── world_model.py
│   │       └── world_model_router.py
│   ├── code_wizard.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── llm_config.json
│   │   └── settings.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── agents
│   │   │   ├── __init__.py
│   │   │   ├── base
│   │   │   │   ├── __init__.py
│   │   │   │   ├── agent_base.py
│   │   │   │   └── base_models.py
│   │   │   ├── core_agents
│   │   │   │   ├── __init__.py
│   │   │   │   ├── agent_types.py
│   │   │   │   ├── broker.py
│   │   │   │   ├── business_agent.py
│   │   │   │   ├── business_plan_agent.py
│   │   │   │   ├── code_generation_agent.py
│   │   │   │   ├── environmental_agent.py
│   │   │   │   ├── llm_agent.py
│   │   │   │   ├── maintenance_agent.py
│   │   │   │   ├── proactive_agent.py
│   │   │   │   ├── reactive_agent.py
│   │   │   │   └── security_agent.py
│   │   │   ├── meta_agents
│   │   │   │   ├── __init__.py
│   │   │   │   ├── agent_design_agent.py
│   │   │   │   ├── architecture_design_agent.py
│   │   │   │   ├── database_agent.py
│   │   │   │   ├── deployment_agent.py
│   │   │   │   ├── domain_modeling_agent.py
│   │   │   │   ├── implementation_agent.py
│   │   │   │   ├── integration_agent.py
│   │   │   │   ├── meta_agents.py
│   │   │   │   ├── meta_mas.py
│   │   │   │   ├── monitoring_agent.py
│   │   │   │   ├── ontology_engineering_agent.py
│   │   │   │   ├── operational_meta_agent.py
│   │   │   │   ├── optimization_agent.py
│   │   │   │   ├── requirements_analysis_agent.py
│   │   │   │   ├── strategic_meta_agent.py
│   │   │   │   ├── tactical_meta_agent.py
│   │   │   │   └── testing_and_verification_agent.py
│   │   │   └── ui_agents
│   │   │       ├── __init__.py
│   │   │       └── onboarding_agent.py
│   │   ├── dependencies.py
│   │   ├── models
│   │   │   ├── Interaction.py
│   │   │   ├── __init__.py
│   │   │   ├── agent
│   │   │   │   ├── __init__.py
│   │   │   │   ├── action.py
│   │   │   │   ├── agent.py
│   │   │   │   ├── agent_role.py
│   │   │   │   ├── agent_skill.py
│   │   │   │   ├── belief.py
│   │   │   │   ├── desire.py
│   │   │   │   ├── goal.py
│   │   │   │   ├── intention.py
│   │   │   │   ├── plan.py
│   │   │   │   └── task.py
│   │   │   ├── ai_assistant.py
│   │   │   ├── architectural_design.py
│   │   │   ├── business
│   │   │   │   ├── __init__.py
│   │   │   │   ├── business_model.py
│   │   │   │   ├── business_plan.py
│   │   │   │   └── business_profile.py
│   │   │   ├── code_generator.py
│   │   │   ├── communication.py
│   │   │   ├── communication_ontology.py
│   │   │   ├── config.py
│   │   │   ├── consistency_checker.py
│   │   │   ├── data_analyzer.py
│   │   │   ├── database
│   │   │   │   ├── __init__.py
│   │   │   │   └── database_schema_generator.py
│   │   │   ├── erp
│   │   │   │   ├── __init__.py
│   │   │   │   └── erp_models.py
│   │   │   ├── graph_models.py
│   │   │   ├── knowledge
│   │   │   │   ├── __init__.py
│   │   │   │   ├── active_knowledge_acquisition.py
│   │   │   │   ├── base.py
│   │   │   │   ├── business_process_manager.py
│   │   │   │   ├── conflict_resolution.py
│   │   │   │   ├── custom_inference.py
│   │   │   │   ├── distributed_knowledge.py
│   │   │   │   ├── domain
│   │   │   │   ├── explanation_generator.py
│   │   │   │   ├── factory.py
│   │   │   │   ├── fnrl.py
│   │   │   │   ├── knowledge_base.py
│   │   │   │   ├── knowledge_converter.py
│   │   │   │   ├── knowledge_graph.py
│   │   │   │   ├── knowledge_management.py
│   │   │   │   ├── knowledge_representation.py
│   │   │   │   ├── ontology
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── business_ontology.owl
│   │   │   │   │   ├── domain_ontology_generator.py
│   │   │   │   │   ├── mabos.owl
│   │   │   │   │   ├── main.py
│   │   │   │   │   ├── meta_ontology.owl
│   │   │   │   │   ├── meta_ontology.ttl
│   │   │   │   │   ├── metamodel_normative.xmi
│   │   │   │   │   ├── natural_language_interface.py
│   │   │   │   │   ├── ontology.py
│   │   │   │   │   ├── ontology_aligner.py
│   │   │   │   │   ├── ontology_generator.py
│   │   │   │   │   ├── ontology_loader.py
│   │   │   │   │   ├── ontology_manager.py
│   │   │   │   │   ├── ontology_reasoner.py
│   │   │   │   │   ├── ontology_version_control.py
│   │   │   │   │   ├── sbvr_metamodel.xml
│   │   │   │   │   ├── svbr_business_ontology.owl
│   │   │   │   │   ├── svbr_xml_vocab.xsd
│   │   │   │   │   └── test_ontology.py
│   │   │   │   ├── question_models.py
│   │   │   │   ├── reasoning
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── htn_planner.py
│   │   │   │   │   ├── inference_result.py
│   │   │   │   │   ├── reasoner.py
│   │   │   │   │   ├── reasoner_doc.md
│   │   │   │   │   ├── reasoning_behavior.py
│   │   │   │   │   ├── reasoning_engine.py
│   │   │   │   │   ├── reasoning_rule.py
│   │   │   │   │   └── temporal_reasoning.py
│   │   │   │   ├── semantic_formulation_generator.py
│   │   │   │   ├── stochastic_kinetic_model.py
│   │   │   │   ├── topic_map.py
│   │   │   │   └── vocabulary_manager.py
│   │   │   ├── llm_decomposer.py
│   │   │   ├── mabos_service_model.py
│   │   │   ├── mas
│   │   │   │   ├── __init__.py
│   │   │   │   ├── mas_modeling_tool.py
│   │   │   │   ├── mas_models.py
│   │   │   │   └── mas_version_control.py
│   │   │   ├── mdd
│   │   │   │   ├── __init__.py
│   │   │   │   ├── archimate_model.py
│   │   │   │   ├── mdd_mas_model.py
│   │   │   │   ├── togaf_adm.py
│   │   │   │   ├── togaf_mdd_models.py
│   │   │   │   └── tropos_mdd_model.py
│   │   │   ├── message.py
│   │   │   ├── model_updates.py
│   │   │   ├── openai_client.py
│   │   │   ├── plan_library.py
│   │   │   ├── repository.py
│   │   │   ├── rules
│   │   │   │   ├── __init__.py
│   │   │   │   ├── rule_parser.py
│   │   │   │   ├── rules.py
│   │   │   │   └── rules_engine.py
│   │   │   ├── runtime_monitoring.py
│   │   │   ├── secure_communication.py
│   │   │   ├── sentence_transformer.py
│   │   │   ├── skills.py
│   │   │   ├── system
│   │   │   │   ├── __init__.py
│   │   │   │   ├── environment.py
│   │   │   │   ├── multi_model_view.py
│   │   │   │   ├── multiagent_system.py
│   │   │   │   ├── organization.py
│   │   │   │   ├── world_model.py
│   │   │   │   └── world_model_provider.py
│   │   │   ├── uml_diagram_generator.py
│   │   │   ├── update_forward_refs.py
│   │   │   ├── utils
│   │   │   │   ├── __init__.py
│   │   │   │   ├── model_init.py
│   │   │   │   └── type_definitions.py
│   │   │   └── version_control.py
│   │   ├── services
│   │   │   ├── __init__.py
│   │   │   ├── action_service.py
│   │   │   ├── agent_communication_service.py
│   │   │   ├── agent_role_service.py
│   │   │   ├── agent_service.py
│   │   │   ├── archimate_service.py
│   │   │   ├── belief_service.py
│   │   │   ├── business_model_service.py
│   │   │   ├── business_onboarding.py
│   │   │   ├── business_plan_service.py
│   │   │   ├── database_service.py
│   │   │   ├── desire_service.py
│   │   │   ├── environment_service.py
│   │   │   ├── erp_service.py
│   │   │   ├── goal_service.py
│   │   │   ├── human_communication_service.py
│   │   │   ├── intention_service.py
│   │   │   ├── knowledge_base_service.py
│   │   │   ├── llm_service.py
│   │   │   ├── mabos_service.py
│   │   │   ├── mas_services.py
│   │   │   ├── mdd_mas_services.py
│   │   │   ├── modeling_service.py
│   │   │   ├── ontology_service.py
│   │   │   ├── organization_service.py
│   │   │   ├── plan_service.py
│   │   │   ├── planning_service.py
│   │   │   ├── question_service.py
│   │   │   ├── reactive_service.py
│   │   │   ├── repository_service.py
│   │   │   ├── rule_engine_service.py
│   │   │   ├── rules_service.py
│   │   │   ├── strategy_service.py
│   │   │   ├── task_manager.py
│   │   │   ├── togaf_mdd_services.py
│   │   │   ├── topic_map_service.py
│   │   │   ├── tropos_mdd_services.py
│   │   │   ├── version_control_service.py
│   │   │   └── world_model_service.py
│   │   ├── tools
│   │   │   ├── __init__.py
│   │   │   ├── llm_manager.py
│   │   │   └── prompts
│   │   │       ├── business_gen_prompt.md
│   │   │       ├── business_gen_prompt_example.md
│   │   │       └── code_engineer
│   │   │           ├── code_evaluation_agent.md
│   │   │           ├── code_generator_agent.md
│   │   │           ├── code_improver_agent.md
│   │   │           ├── code_rater_agent.md
│   │   │           └── diagram.plantuml
│   │   └── utils
│   │       ├── __init__.py
│   │       ├── agent_executor.py
│   │       ├── anthropic_integration.py
│   │       ├── file_utils.py
│   │       └── nlputils.py
│   ├── data
│   │   ├── 2022-NAICS-Codes-listed-numerically-2-Digit-through-6-Digit.xlsx
│   │   ├── 2022_naics_codes.csv
│   │   └── business_description.md
│   ├── db
│   │   ├── __init__.py
│   │   ├── arango_db_client.py
│   │   ├── arangodb.py
│   │   ├── database.py
│   │   ├── database_models.py
│   │   ├── db_integration.py
│   │   ├── storage_backend.py
│   │   └── togaf_questions.py
│   ├── exceptions.py
│   ├── integration
│   │   ├── __init__.py
│   │   └── mdd_mas_integration.py
│   └── repositories
│       ├── __init__.py
│       ├── models
│       │   ├── goal_objective_service_diagram.xml
│       │   └── state_machine_uml.xml
│       ├── ontologies
│       └── rules
│           ├── rules.csv
│           └── rules.xml
├── docs
│   ├── COMPaaS.md
│   ├── Screenshot 2024-08-27 at 11.31.46 AM.png
│   ├── The Key to Artificial Minds - Ontology.txt
│   ├── The Key to Artificial Minds Ontology.md
│   ├── acl-doc.md
│   ├── action_actiondb_doc.md
│   ├── agent_docs.md
│   ├── bpmn_example.md
│   ├── business_goals.md
│   ├── business_model.md
│   ├── business_plan.md
│   ├── business_rules.md
│   ├── catalog_matrix_diagram.md
│   ├── code_evaluation_agent.md
│   ├── code_generator_agent.md
│   ├── code_improver_agent.md
│   ├── code_rater_agent.md
│   ├── description.md
│   ├── explaintion.md
│   ├── file-folder-structure.md
│   ├── files.md
│   ├── knowledge_constructionist.md
│   ├── knowledge_management.md
│   ├── multiAgent-system-README-documentation.md
│   ├── ontology-llm-reasoning_notes.md
│   ├── ontology-topicmap.md
│   ├── ontology_generation_doc.md
│   ├── ontology_generator.md
│   ├── pade-framework.md
│   ├── production-improvments.md
│   ├── readme-tgest.md
│   ├── reasoner.md
│   ├── requirements_analysis_agent-docs.md
│   ├── rules_engine_doc.md
│   ├── tree_structure.md
│   ├── tropos_example.md
│   └── xml-modeling-prompt.md
├── export
├── main.py
├── pyproject.toml
├── requirements.txt
├── scripts
│   ├── __init__.py
│   ├── generate_and_validate_ontology.py
│   ├── run_webvowl.sh
│   └── seed_arangodb.py
├── tests
│   ├── @data
│   │   ├── artists.json
│   │   ├── artworks.json
│   │   ├── categories.json
│   │   ├── collections.json
│   │   ├── customers.json
│   │   ├── historical_sales.json
│   │   ├── orders.json
│   │   ├── print_on_demand_suppliers.json
│   │   ├── vividwalls_ontology.owl
│   │   └── vividwalls_ontology.rdf
│   ├── __init__.py
│   ├── e2e
│   │   ├── __init__.py
│   │   ├── test_agent_interaction.py
│   │   ├── test_system_integration.py
│   │   └── test_user_workflow.py
│   ├── test_business_description.md
│   ├── test_config_loading.py
│   ├── test_ecommerce_onboarding.py
│   └── unit
│       ├── __init__.py
│       ├── test_agent_base.py
│       ├── test_agent_design_agent.py
│       ├── test_agents.py
│       ├── test_architecture_design_agent.py
│       ├── test_broker.py
│       ├── test_business_agent.py
│       ├── test_business_plan_agent.py
│       ├── test_database_agent.py
│       ├── test_environmental_agent.py
│       ├── test_goals.py
│       ├── test_implementation_agent.py
│       ├── test_integration_agent.py
│       ├── test_knowledge_bases.py
│       ├── test_llm_agent.py
│       ├── test_maintenance_agent.py
│       ├── test_meta_mas.py
│       ├── test_monitoring_agent.py
│       ├── test_ontology.py
│       ├── test_ontology_engineering_agent.py
│       ├── test_operational_meta_agent.py
│       ├── test_optimization_agent.py
│       ├── test_plans.py
│       ├── test_proactive_agent.py
│       ├── test_reactive_agent.py
│       ├── test_requirements_analysis_agent.py
│       ├── test_strategic_meta_agent.py
│       └── test_tactical_meta_agent.py
└── ui
    ├── app.py
    └── templates
        └── index.html

45 directories, 364 files
(mabos-standalone) (base) ➜  mabos-standalone git:(pade-framework) ✗ tree -I '__pycache__|NuSMV-2.6.0|pynusmv' -L 2 --charset=ascii
.
|-- __init__.py
|-- app
|   |-- api
|   |-- code_wizard.py
|   |-- config
|   |-- core
|   |-- data
|   |-- db
|   |-- exceptions.py
|   |-- integration
|   `-- repositories
|-- docs
|   |-- COMPaaS.md
|   |-- README.md
|   |-- Screenshot 2024-08-27 at 11.31.46 AM.png
|   |-- The Key to Artificial Minds - Ontology.txt
|   |-- The Key to Artificial Minds Ontology.md
|   |-- acl-doc.md
|   |-- action_actiondb_doc.md
|   |-- agent_docs.md
|   |-- bpmn_example.md
|   |-- business_goals.md
|   |-- business_model.md
|   |-- business_plan.md
|   |-- business_rules.md
|   |-- catalog_matrix_diagram.md
|   |-- code_evaluation_agent.md
|   |-- code_generator_agent.md
|   |-- code_improver_agent.md
|   |-- code_rater_agent.md
|   |-- description.md
|   |-- explaintion.md
|   |-- file-folder-structure.md
|   |-- files.md
|   |-- knowledge_constructionist.md
|   |-- knowledge_management.md
|   |-- multiAgent-system-README-documentation.md
|   |-- ontology-llm-reasoning_notes.md
|   |-- ontology-topicmap.md
|   |-- ontology_generation_doc.md
|   |-- ontology_generator.md
|   |-- pade-framework.md
|   |-- production-improvments.md
|   |-- readme-tgest.md
|   |-- reasoner.md
|   |-- requirements_analysis_agent-docs.md
|   |-- rules_engine_doc.md
|   |-- tree_structure.md
|   |-- tropos_example.md
|   `-- xml-modeling-prompt.md
|-- export
|-- main.py
|-- pyproject.toml
|-- requirements.txt
|-- scripts
|   |-- __init__.py
|   |-- generate_and_validate_ontology.py
|   |-- run_webvowl.sh
|   `-- seed_arangodb.py
|-- tests
|   |-- @data
|   |-- __init__.py
|   |-- e2e
|   |-- test_business_description.md
|   |-- test_config_loading.py
|   |-- test_ecommerce_onboarding.py
|   `-- unit
`-- ui
    |-- app.py
    `-- templates