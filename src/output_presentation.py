```python
from flask import Flask, render_template, request, redirect, url_for, flash
from models.task import Task

app = Flask(__name__)

@app.route('/output', methods=['GET'])
def present_output():
    task_id = request.args.get('task_id')
    task = Task.query.get(task_id)
    if task:
        return render_template('output.html', task=task)
    else:
        flash('Task not found', 'error')
        return redirect(url_for('dashboard'))

@app.route('/save_output', methods=['POST'])
def save_output():
    task_id = request.form.get('task_id')
    task = Task.query.get(task_id)
    if task:
        task.status = 'completed'
        task.save()
        flash('Output saved successfully', 'success')
    else:
        flash('Task not found', 'error')
    return redirect(url_for('dashboard'))

@app.route('/new_task', methods=['GET'])
def start_new_task():
    return redirect(url_for('task_input'))

@app.route('/exit', methods=['GET'])
def exit_application():
    return redirect(url_for('login'))
```