```javascript
// Importing necessary modules
import { authenticateUser } from './user_authentication.js';
import { cloneGitRepo } from './git_repository_management.js';
import { uploadFile } from './file_upload.js';
import { inputTask } from './task_input.js';
import { manageAIagentTask } from './ai_agent_task_management.js';
import { executeTask } from './task_execution.js';
import { presentOutput } from './output_presentation.js';

// DOM Elements
const loginForm = document.getElementById('login-form');
const gitCloneInput = document.getElementById('git-clone-input');
const fileUploadInput = document.getElementById('file-upload-input');
const taskInput = document.getElementById('task-input');
const saveOutputBtn = document.getElementById('save-output-btn');
const newTaskBtn = document.getElementById('new-task-btn');
const exitBtn = document.getElementById('exit-btn');

// Event Listeners
loginForm.addEventListener('submit', authenticateUser);
gitCloneInput.addEventListener('change', cloneGitRepo);
fileUploadInput.addEventListener('change', uploadFile);
taskInput.addEventListener('change', inputTask);
saveOutputBtn.addEventListener('click', presentOutput);
newTaskBtn.addEventListener('click', startNewTask);
exitBtn.addEventListener('click', exitApplication);

// Function to start a new task
function startNewTask() {
    // Clear the task input and output fields
    taskInput.value = '';
    document.getElementById('task-output').innerHTML = '';

    // Enable the task input field
    taskInput.disabled = false;
}

// Function to exit the application
function exitApplication() {
    // Log the user out and redirect to the login page
    fetch('/logout', {
        method: 'POST'
    }).then(response => {
        if (response.ok) {
            window.location.href = '/login';
        } else {
            console.error('Failed to log out');
        }
    });
}
```