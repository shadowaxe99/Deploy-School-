```javascript
// Function to execute task using AI agents
function executeTask(task) {
    // Create a new XMLHttpRequest object
    let xhr = new XMLHttpRequest();

    // Configure the request
    xhr.open('POST', '/execute-task', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    // Define what happens on successful data submission
    xhr.onload = function(event) {
        // Parse the JSON response
        let jsonResponse = JSON.parse(xhr.responseText);

        // Check if the task execution was successful
        if (jsonResponse.status === 'success') {
            // Update the task output in the DOM
            document.getElementById('task-output').textContent = jsonResponse.output;

            // Emit a custom event to indicate task execution success
            let event = new CustomEvent('TASK_EXECUTION_SUCCESS', { detail: jsonResponse });
            document.dispatchEvent(event);
        } else {
            // Emit a custom event to indicate task execution failure
            let event = new CustomEvent('TASK_EXECUTION_FAILURE', { detail: jsonResponse });
            document.dispatchEvent(event);
        }
    };

    // Define what happens in case of error
    xhr.onerror = function(event) {
        // Emit a custom event to indicate task execution failure
        let event = new CustomEvent('TASK_EXECUTION_FAILURE', { detail: { status: 'error', message: 'An error occurred while executing the task.' } });
        document.dispatchEvent(event);
    };

    // Send the request with the task data
    xhr.send(JSON.stringify({ task: task }));
}

// Listen for the 'TASK_INPUT_SUCCESS' event
document.addEventListener('TASK_INPUT_SUCCESS', function(event) {
    // Execute the task using AI agents
    executeTask(event.detail.task);
});
```