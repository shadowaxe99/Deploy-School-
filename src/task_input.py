```python
from flask import request, jsonify
from openai import OpenAIAPI
from models.task import Task
from utilities import db

WHISPER_API_KEY = "your-whisper-api-key"

def inputTask():
    task_description = request.form.get('task-input')
    user_id = request.form.get('user-id')

    # Initialize OpenAI API
    openai_api = OpenAIAPI(WHISPER_API_KEY)

    # Process task input using Whisper API
    try:
        processed_task = openai_api.process_input(task_description)
    except Exception as e:
        return jsonify({"message": "TASK_INPUT_FAILURE", "error": str(e)}), 400

    # Save task to database
    new_task = Task(task_description=processed_task, user_id=user_id)
    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "TASK_INPUT_SUCCESS", "task": new_task.serialize()}), 200
```