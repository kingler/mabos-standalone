import os
import sys

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from flask import Flask, jsonify, render_template, request

from app.agents.ui_agents.onboarding_agent import OnboardingAgent
from app.db.arango_db_client import ArangoDBClient

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/onboard', methods=['POST'])
async def onboard():
    use_example = request.form.get('use_example') == 'true'
    
    db_client = ArangoDBClient()  # You might need to adjust this based on your actual implementation
    onboarding_agent = await OnboardingAgent.create(db_client=db_client)
    
    result = await onboarding_agent.conduct_onboarding(use_example=use_example)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
