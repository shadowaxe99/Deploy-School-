```javascript
// DOM Elements
const taskOutput = document.getElementById('task-output');
const saveOutputBtn = document.getElementById('save-output-btn');
const newTaskBtn = document.getElementById('new-task-btn');
const exitBtn = document.getElementById('exit-btn');

// Event Listeners
saveOutputBtn.addEventListener('click', saveOutput);
newTaskBtn.addEventListener('click', startNewTask);
exitBtn.addEventListener('click', exitApplication);

// Function to save output
function saveOutput() {
    const output = taskOutput.innerText;
    if (output) {
        // Save output logic here
        // This could be a call to the backend to save the output in the database
        console.log('Output saved successfully');
    } else {
        console.error('No output to save');
    }
}

// Function to start a new task
function startNewTask() {
    // Clear the task output
    taskOutput.innerText = '';
    // Logic to start a new task here
    // This could be redirecting the user to the task input page
    console.log('New task started');
}

// Function to exit the application
function exitApplication() {
    // Logic to exit the application here
    // This could be logging out the user and redirecting them to the login page
    console.log('Application exited');
}

// Function to present output
function presentOutput(output) {
    if (output) {
        taskOutput.innerText = output;
        console.log('Output presented successfully');
    } else {
        console.error('No output to present');
    }
}
```