function generateNewPost() {
    fetch('/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic: "Computer Vision latest trends" })
    }).then(res => res.json()).then(data => {
        if(data.success) location.reload();
    });
}

function takeAction(id, actionType) {
    fetch('/api/action', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: id, action: actionType })
    }).then(res => res.json()).then(data => {
        if(data.success) {
            alert('Action completed! New status: ' + data.status);
            location.reload();
        } else {
            alert('Failed. Check API keys and console.');
        }
    });
}