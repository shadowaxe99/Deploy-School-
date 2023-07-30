```javascript
// AI Agent Task Management

// Importing dependencies
import axios from 'axios';

// Function to manage AI agent task
function manageAIagentTask(taskInput) {
    // API endpoint for AI agent task management
    const endpoint = '/api/ai-agent-task-management';

    // Request body
    const requestBody = {
        task: taskInput
    };

    // Making a POST request to the server
    axios.post(endpoint, requestBody)
        .then(response => {
            // If the task is successfully communicated to the AI agent
            if (response.data.status === 'TASK_INPUT_SUCCESS') {
                console.log('Task successfully communicated to the AI agent.');
            } else {
                // If there is an error in communicating the task to the AI agent
                console.error('Error in communicating the task to the AI agent.');
            }
        })
        .catch(error => {
            // If there is an error in making the request
            console.error('Error in making the request to the server:', error);
        });
}

export default manageAIagentTask;
```