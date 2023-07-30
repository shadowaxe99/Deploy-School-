```python
from flask import Flask, request, jsonify
from ai_agent_factory import AI_Agent_Factory
from models.task import Task
from utilities import update_task_status

app = Flask(__name__)

@app.route('/execute_task', methods=['POST'])
def execute_task():
    task_id = request.json.get('task_id')
    task = Task.get_by_id(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404

    ai_agent = AI_Agent_Factory.create_agent(task.task_description)
    try:
        task_output = ai_agent.execute_task()
        task.output = task_output
        task.status = 'completed'
        task.save()
        update_task_status(task_id, 'completed')
        return jsonify({'message': 'Task executed successfully', 'output': task_output}), 200
    except Exception as e:
        task.status = 'failed'
        task.save()
        update_task_status(task_id, 'failed')
        return jsonify({'message': 'Task execution failed', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```