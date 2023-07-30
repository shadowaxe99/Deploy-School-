```python
from flask import Flask, request, jsonify
from src.ai_agent_factory import createAIagent
from src.models.task import Task
from src.utilities import update_task_status
from src.models.user import get_user
from openai import OpenAIAPI

app = Flask(__name__)

@app.route('/manageAIagentTask', methods=['POST'])
def manageAIagentTask():
    task_id = request.json.get('task_id')
    user_id = request.json.get('user_id')

    # Fetch the user and task from the database
    user = get_user(user_id)
    task = Task.query.get(task_id)

    if not user or not task:
        return jsonify({"message": "User or Task not found"}), 404

    # Create an AI agent
    ai_agent = createAIagent(user)

    # Process the task using the Whisper API
    whisper_api = OpenAIAPI(api_key=app.config['WHISPER_API_KEY'])
    task_output = whisper_api.process(task.task_description)

    # Update the task status and output
    task.status = "completed"
    task.output = task_output
    update_task_status(task)

    return jsonify({"message": "Task executed successfully", "output": task_output}), 200
```