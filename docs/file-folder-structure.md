.
├── __init__.py
├── app
│   ├── api
│   │   ├── __init__.py
│   │   ├── routes
│   │   │   ├── __init__.py
│   │   │   ├── actions.py
│   │   │   ├── agent_roles.py
│   │   │   ├── agents.py
│   │   │   ├── beliefs.py
│   │   │   ├── business_models.py
│   │   │   ├── business_plan.py
│   │   │   ├── communication.py
│   │   │   ├── desires.py
│   │   │   ├── environment.py
│   │   │   ├── erp.py
│   │   │   ├── erp_router.py
│   │   │   ├── goals.py
│   │   │   ├── intentions.py
│   │   │   ├── knowledge_bases.py
│   │   │   ├── mabos_routers.py
│   │   │   ├── mas.py
│   │   │   ├── mas_modeling.py
│   │   │   ├── mas_router.py
│   │   │   ├── mdd_mas.py
│   │   │   ├── ontology.py
│   │   │   ├── organization.py
│   │   │   ├── planning.py
│   │   │   ├── plans.py
│   │   │   ├── question.py
│   │   │   ├── question_router.py
│   │   │   ├── repository.py
│   │   │   ├── rules_engine.py
│   │   │   ├── tasks.py
│   │   │   ├── togaf_mdd.py
│   │   │   ├── topic_map.py
│   │   │   ├── tropos_mdd.py
│   │   │   ├── version_control.py
│   │   │   ├── world_model.py
│   │   │   └── world_model_router.py
│   │   ├── schemas
│   │   │   └── __init__.py
│   │   └── services
│   │       └── __init__.py
│   ├── communication
│   │   ├── __init__.py
│   │   └── agent_communication.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── agents
│   │   │   ├── __init__.py
│   │   │   ├── agent_types.py
│   │   │   ├── base
│   │   │   │   ├── __init__.py
│   │   │   │   └── agent_base.py
│   │   │   ├── business_plan_agent.py
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
│   │   │   ├── onboarding_agent.py
│   │   │   ├── proactive_agent.py
│   │   │   ├── reactive_agent.py
│   │   │   └── ui_agents
│   │   │       ├── __init__.py
│   │   │       └── onboarding_agent.py
│   │   ├── models
│   │   │   ├── Interaction.py
│   │   │   ├── __init__.py
│   │   │   ├── active_knowledge_acquisition.py
│   │   │   ├── agent
│   │   │   │   ├── agent.py
│   │   │   │   ├── agent_role.py
│   │   │   │   ├── belief.py
│   │   │   │   ├── desire.py
│   │   │   │   ├── goal.py
│   │   │   │   ├── intention.py
│   │   │   │   └── plan.py
│   │   │   ├── ai_assistant.py
│   │   │   ├── archimate_model.py
│   │   │   ├── architectural_design.py
│   │   │   ├── base_models.py
│   │   │   ├── business_model.py
│   │   │   ├── business_plan.py
│   │   │   ├── code_generator.py
│   │   │   ├── communication_ontology.py
│   │   │   ├── config.py
│   │   │   ├── conflict_resolution.py
│   │   │   ├── consistency_checker.py
│   │   │   ├── core
│   │   │   │   ├── __init__.py
│   │   │   │   ├── action.py
│   │   │   │   └── mdd_mas_model.py
│   │   │   ├── custom_inference.py
│   │   │   ├── data_analyzer.py
│   │   │   ├── db_integration.py
│   │   │   ├── distributed_knowledge.py
│   │   │   ├── domain
│   │   │   │   ├── business_process_manager.py
│   │   │   │   ├── knowledge_graph.py
│   │   │   │   ├── ontology.py
│   │   │   │   └── topic_map.py
│   │   │   ├── domain_ontology_generator.py
│   │   │   ├── environmental_agent.py
│   │   │   ├── erp_models.py
│   │   │   ├── explanation_generator.py
│   │   │   ├── fnrl.py
│   │   │   ├── graph_models.py
│   │   │   ├── llm_decomposer.py
│   │   │   ├── mabos_service_model.py
│   │   │   ├── mas
│   │   │   │   ├── __init__.py
│   │   │   │   ├── mas_modeling_tool.py
│   │   │   │   ├── mas_models.py
│   │   │   │   └── mas_version_control.py
│   │   │   ├── message.py
│   │   │   ├── model_updates.py
│   │   │   ├── multi_model_view.py
│   │   │   ├── ontology_generator.py
│   │   │   ├── ontology_loader.py
│   │   │   ├── ontology_manager.py
│   │   │   ├── ontology_types.py
│   │   │   ├── openai_client.py
│   │   │   ├── plan_library.py
│   │   │   ├── question_models.py
│   │   │   ├── repository.py
│   │   │   ├── rules.py
│   │   │   ├── runtime_monitoring.py
│   │   │   ├── secure_communication.py
│   │   │   ├── sentence_transformer.py
│   │   │   ├── skills.py
│   │   │   ├── stochastic_kinetic_model.py
│   │   │   ├── system
│   │   │   │   ├── environment.py
│   │   │   │   ├── multiagent_system.py
│   │   │   │   ├── organization.py
│   │   │   │   └── world_model.py
│   │   │   ├── task.py
│   │   │   ├── togaf_adm.py
│   │   │   ├── togaf_mdd_models.py
│   │   │   ├── tropos_mdd_model.py
│   │   │   ├── uml_diagram_generator.py
│   │   │   ├── update_forward_refs.py
│   │   │   ├── utils
│   │   │   │   ├── __init__.py
│   │   │   │   ├── model_init.py
│   │   │   │   └── type_definitions.py
│   │   │   ├── version_control.py
│   │   │   └── world_model_provider.py
│   │   ├── services
│   │   │   ├── __init__.py
│   │   │   ├── action_service.py
│   │   │   ├── agent_communication_service.py
│   │   │   ├── agent_role_service.py
│   │   │   ├── agent_service.py
│   │   │   ├── belief_service.py
│   │   │   ├── business_model_service.py
│   │   │   ├── business_plan_service.py
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
│   │   │   └── llm_manager.py
│   │   └── utils
│   │       ├── __init__.py
│   │       ├── agent_executor.py
│   │       ├── anthropic_integration.py
│   │       └── nlputils.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── arango_db_client.py
│   │   ├── arangodb.py
│   │   ├── database.py
│   │   ├── db_integration.py
│   │   └── togaf-questions.py
│   ├── dependencies.py
│   ├── exceptions.py
│   ├── integration
│   │   ├── __init__.py
│   │   └── mdd_mas_integration.py
│   ├── knowledge
│   │   ├── __init__.py
│   │   ├── knowledge_base.py
│   │   ├── knowledge_converter.py
│   │   ├── knowledge_representation.py
│   │   ├── ontologies
│   │   │   ├── business_ontology.owl
│   │   │   ├── mabos.owl
│   │   │   ├── meta_ontology.owl
│   │   │   └── meta_ontology.ttl
│   │   └── reasoning
│   │       ├── __init__.py
│   │       ├── htn_planner.py
│   │       ├── reasoner.py
│   │       ├── reasoning_engine.py
│   │       ├── rules_engine.py
│   │       ├── symbolic_planner.py
│   │       └── temporal_reasoning.py
│   ├── repositories
│   │   ├── __init__.py
│   │   ├── models
│   │   │   ├── goal_objective_service_diagram.xml
│   │   │   └── state_machine_uml.xml
│   │   ├── ontologies
│   │   │   ├── business_ontology.owl
│   │   │   ├── mabos.owl
│   │   │   └── meta_ontology.owl
│   │   └── rules
│   │       ├── rules.csv
│   │       └── rules.xml
│   └── tools
│       └── __init__.py
├── config
│   ├── __init__.py
│   ├── llm_config.yaml
│   └── settings.py
├── docs
│   ├── README.md
│   ├── bpmn_example.md
│   ├── business_goals.md
│   ├── business_model.md
│   ├── business_plan.md
│   ├── business_rules.md
│   ├── catalog_matrix_diagram.md
│   ├── description.md
│   ├── explaintion.md
│   ├── knowledge_constructionist.md
│   ├── knowledge_management.md
│   ├── ontology-topicmap.md
│   ├── readme-tgest.md
│   ├── requirements_analysis_agent-docs.md
│   └── tropos_example.md
├── main.py
├── pyproject.toml
├── requirements.txt
├── scripts
│   └── __init__.py
└── tests
    ├── e2e
    │   ├── __init__.py
    │   ├── test_agent_interaction.py
    │   ├── test_system_integration.py
    │   └── test_user_workflow.py
    └── unit
        ├── __init__.py
        ├── test_agents.py
        ├── test_goals.py
        ├── test_knowledge_bases.py
        ├── test_ontology.py
        └── test_plans.py