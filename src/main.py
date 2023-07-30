```python
from flask import Flask, render_template, request, redirect, url_for, session
from src.user_authentication import authenticateUser
from src.git_repository_management import cloneGitRepo
from src.file_upload import uploadFile
from src.task_input import inputTask
from src.ai_agent_task_management import manageAIagentTask
from src.task_execution import executeTask
from src.output_presentation import presentOutput
from src.models.user import User
from src.models.task import Task
from src.utilities import DATABASE_URI, SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = authenticateUser(username, password)
    if user:
        session['username'] = user.username
        return redirect(url_for('dashboard'))
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('home'))
    return render_template('dashboard.html')

@app.route('/clone', methods=['POST'])
def clone():
    repo_url = request.form['repo_url']
    cloneGitRepo(repo_url)
    return redirect(url_for('dashboard'))

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    uploadFile(file)
    return redirect(url_for('dashboard'))

@app.route('/task', methods=['POST'])
def task():
    task_description = request.form['task_description']
    task = inputTask(task_description)
    manageAIagentTask(task)
    executeTask(task)
    output = presentOutput(task)
    return render_template('output.html', output=output)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
```