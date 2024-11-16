# Multi-Agent Business Optimization System (MABOS)

## Project Overview

MABOS is a sophisticated multi-agent system designed to assist businesses in achieving their goals through advanced AI-driven reasoning and decision-making processes. The system leverages various AI/ML techniques, including symbolic planning, semantic search, and multi-modal reasoning to provide intelligent insights and recommendations.

## Key Features

- Multi-agent system using PADE framework
- Advanced reasoning engine with multiple reasoning methods
- Symbolic planning for complex decision-making
- Semantic search functionality using vector embeddings
- Integration with external Language Models (LLMs)
- Business goal tracking and optimization
- Operational efficiency analysis
- Customer satisfaction monitoring
- Market analysis and prediction
- Sustainability metrics tracking
- RESTful API for interacting with the system
- React-based frontend for user interaction
- User authentication and role-based access control
- Email verification for new user registration
- HTTPS support for secure communication
- Two-Factor Authentication (2FA)
- Automated security scanning with OWASP ZAP

## Tech Stack

- **Backend**: 
  - Core Framework: PADE (Python Agent DEvelopment)
  - Programming Language: Python
  - Database: ArangoDB
  - API Framework: FastAPI
- **Frontend**:
  - Framework: React
- **AI/ML Libraries**: 
  - sympy
  - pyres
  - pysmt
  - z3
  - sentence_transformers
- **Additional Libraries**:
  - pydantic
  - numpy
  - asyncio
  - python-dotenv
  - python-owasp-zap-v2.4

For a detailed overview of the technology stack, please refer to the `claudeDev_docs/techStack.md` file.

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 14+
- ArangoDB 3.7+
- Redis 6+
- OpenSSL (for generating SSL certificates)
- OWASP ZAP 2.10+

### Backend Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-repo/mabos.git
   cd mabos
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up ArangoDB:
   - Install ArangoDB following the instructions for your operating system: https://www.arangodb.com/download/
   - Start the ArangoDB service

5. Set up Redis:
   - Install Redis following the instructions for your operating system: https://redis.io/download
   - Start the Redis service

6. Set up environment variables:
   - Copy the `.env.example` file to `.env`
   - Fill in the necessary environment variables, including database credentials

7. Generate SSL certificates for HTTPS:
   ```
   python scripts/generate_ssl_cert.py
   ```

8. Run the API server with HTTPS:
   ```
   uvicorn src.api.main:app --reload --ssl-keyfile=localhost.key --ssl-certfile=localhost.crt
   ```

   The API will be available at `https://localhost:8000`. You can access the interactive API documentation at `https://localhost:8000/docs`.

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install the required dependencies:
   ```
   npm install
   ```

3. Generate SSL certificates for HTTPS (if not already done):
   ```
   openssl req -x509 -newkey rsa:2048 -keyout localhost.key -out localhost.crt -days 365 -nodes -subj "/CN=localhost"
   ```

4. Start the development server with HTTPS:
   ```
   npm run start:https
   ```

   The frontend will be available at `https://localhost:3000`.

## Running the Full System

1. Start the ArangoDB service (if not already running)
2. Start the Redis service (if not already running)

3. In one terminal, start the backend server:
   ```
   cd /path/to/mabos
   source venv/bin/activate
   uvicorn src.api.main:app --reload --ssl-keyfile=localhost.key --ssl-certfile=localhost.crt
   ```

4. In another terminal, start the frontend development server:
   ```
   cd /path/to/mabos/frontend
   npm run start:https
   ```

5. Open your web browser and navigate to `https://localhost:3000` to access the MABOS application.

## Security Scanning with OWASP ZAP

### Installing OWASP ZAP

1. Download OWASP ZAP from the official website: https://www.zaproxy.org/download/
2. Install ZAP following the instructions for your operating system

### Running ZAP Scans

1. Ensure that both the backend and frontend servers are running
2. Open a terminal and navigate to the project root directory
3. Activate the virtual environment
4. Run the ZAP scan script:
   ```
   python scripts/run_zap_scan.py
   ```
5. The script will start ZAP, perform a spider crawl of the application, run active and passive scans, and generate a report

### Automated Security Scanning

This project uses GitHub Actions to run automated security scans:

- Scans are performed on every pull request to the main branch
- Nightly scans are scheduled to run at 2 AM UTC every day
- Scan reports are uploaded as artifacts in the GitHub Actions workflow
- Slack notifications are sent with the scan results (requires Slack webhook configuration)

To view the scan results:
1. Go to the "Actions" tab in the GitHub repository
2. Click on the latest "Security Scan" workflow run
3. Download the "zap-scan-report" artifact to view the full HTML report

For more details on the security scanning process, please refer to the `.github/workflows/security-scan.yml` file.

### Scan Reports

After running the ZAP scan, you can find the HTML report in the `security_reports` directory. The report will be named `zap_report_YYYYMMDD-HHMMSS.html`, where YYYYMMDD-HHMMSS is the timestamp of when the scan was run.

Review these reports regularly to identify and address any security vulnerabilities in the application.

## Usage

1. Register a new account and verify your email
2. Log in to the application
3. Set up Two-Factor Authentication for enhanced security
4. Use the web interface to create, view, and manage business goals
5. View efficiency analyses for individual goals and overall performance
6. Receive AI-driven recommendations for improving goal achievement and operational efficiency

## API Endpoints

For a full list of available API endpoints and their usage, please refer to the API documentation available at `https://localhost:8000/docs` when the backend server is running.

## Project Structure

- `src/`: Main application code
  - `api/`: API-related code
  - `agents/`: Agent implementations
  - `reasoning/`: Reasoning engine implementation
  - `db/`: Database-related code
  - `search/`: Semantic search implementation
  - `business/`: Business logic implementation
- `tests/`: Unit and integration tests
- `config/`: Configuration files
- `claudeDev_docs/`: Project documentation
- `frontend/`: React-based frontend application
- `scripts/`: Utility scripts, including ZAP scan script
- `.github/workflows/`: GitHub Actions workflow definitions

## Contributing

Please refer to the `CONTRIBUTING.md` file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

For more detailed information about the project, please refer to the documentation in the `claudeDev_docs/` directory.
