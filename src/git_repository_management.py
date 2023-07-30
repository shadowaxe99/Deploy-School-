```python
import os
import subprocess
from flask import Blueprint, request, jsonify

git_blueprint = Blueprint('git_blueprint', __name__)

@git_blueprint.route('/clone', methods=['POST'])
def clone_git_repo():
    data = request.get_json()
    git_url = data.get('GIT_REPO_URL')
    if not git_url:
        return jsonify({'message': 'GIT_CLONE_FAILURE', 'details': 'No repository URL provided'}), 400

    try:
        subprocess.check_call(['git', 'clone', git_url])
        return jsonify({'message': 'GIT_CLONE_SUCCESS', 'details': 'Repository cloned successfully'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'message': 'GIT_CLONE_FAILURE', 'details': str(e)}), 500
```