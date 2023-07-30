```javascript
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    let username = document.getElementById('username-input').value;
    let password = document.getElementById('password-input').value;

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === 'LOGIN_SUCCESS') {
            window.location.href = '/dashboard';
        } else if (data.message === 'LOGIN_FAILURE') {
            alert('Invalid username or password. Please try again.');
        }
    })
    .catch(error => console.error('Error:', error));
});
```