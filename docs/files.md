├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── agent_endpoints.py
│   │   │   └── other_endpoints.py
│   │   └── dependencies.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── agent_model.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── agent_schema.py
│   │
│   └── services/
│       ├── __init__.py
│       └── agent_service.py
│
├── agents/
│   ├── __init__.py
│   ├── base_agent.py
│   └── specific_agents/
│       ├── __init__.py
│       ├── agent1.py
│       └── agent2.py
│
├── tests/
│   ├── __init__.py
│   ├── test_api/
│   │   ├── __init__.py
│   │   └── test_agent_endpoints.py
│   └── test_agents/
│       ├── __init__.py
│       └── test_specific_agents.py
│
├── alembic/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
│
├── logs/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── run.py