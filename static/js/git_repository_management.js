```javascript
// Function to clone Git repository
function cloneGitRepo() {
    const gitCloneInput = document.getElementById('git-clone-input');
    const gitRepoUrl = gitCloneInput.value;

    if (!gitRepoUrl) {
        alert('Please enter a Git repository URL');
        return;
    }

    fetch('/clone-repo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: gitRepoUrl }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('Git repository cloned successfully');
            gitCloneInput.value = '';
        } else {
            alert('Failed to clone Git repository: ' + data.error);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Event listener for Git clone button
document.getElementById('git-clone-btn').addEventListener('click', cloneGitRepo);
```