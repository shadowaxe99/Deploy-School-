```python
import os
import hashlib
from flask import flash

def set_flask_env_variables():
    os.environ['FLASK_APP'] = 'main.py'
    os.environ['FLASK_ENV'] = 'development'
    os.environ['DATABASE_URI'] = 'sqlite:///site.db'
    os.environ['SECRET_KEY'] = 'your-secret-key'
    os.environ['WHISPER_API_KEY'] = 'your-whisper-api-key'
    os.environ['DOCKER_COMPOSE_FILE'] = 'docker-compose.yml'
    os.environ['GIT_REPO_URL'] = 'your-git-repo-url'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validate_password(hashed_password, user_password):
    return hashed_password == hashlib.sha256(user_password.encode()).hexdigest()

def flash_messages(message_name):
    messages = {
        'LOGIN_SUCCESS': 'Logged in successfully.',
        'LOGIN_FAILURE': 'Login failed. Please check your credentials.',
        'GIT_CLONE_SUCCESS': 'Git repository cloned successfully.',
        'GIT_CLONE_FAILURE': 'Failed to clone Git repository.',
        'FILE_UPLOAD_SUCCESS': 'File uploaded successfully.',
        'FILE_UPLOAD_FAILURE': 'Failed to upload file.',
        'TASK_INPUT_SUCCESS': 'Task input successful.',
        'TASK_INPUT_FAILURE': 'Failed to input task.',
        'TASK_EXECUTION_SUCCESS': 'Task executed successfully.',
        'TASK_EXECUTION_FAILURE': 'Failed to execute task.',
        'OUTPUT_PRESENTATION_SUCCESS': 'Output presented successfully.',
        'OUTPUT_PRESENTATION_FAILURE': 'Failed to present output.',
    }
    flash(messages.get(message_name, 'An unknown error occurred.'))
```