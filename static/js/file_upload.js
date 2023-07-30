```javascript
document.getElementById('file-upload-input').addEventListener('change', uploadFile);

function uploadFile(event) {
    let file = event.target.files[0];
    let formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert(FILE_UPLOAD_SUCCESS);
        } else {
            alert(FILE_UPLOAD_FAILURE);
        }
    })
    .catch(error => console.error('Error:', error));
}
```