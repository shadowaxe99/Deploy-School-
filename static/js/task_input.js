```javascript
document.getElementById('task-input').addEventListener('submit', function(event) {
    event.preventDefault();

    let taskDescription = document.getElementById('task-input').value;

    if (taskDescription) {
        fetch('/api/task', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ task_description: taskDescription }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('Task input successful');
                document.getElementById('task-input').value = '';
            } else {
                alert('Task input failed: ' + data.message);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    } else {
        alert('Please input a task');
    }
});
```