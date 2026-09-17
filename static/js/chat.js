function sendChatMessage() {
    let inputField = document.getElementById("chatInput");
    let chatBox = document.getElementById("chatBox");
    let draftText = document.getElementById("draftText");
    
    let message = inputField.value.trim();
    if (!message) return;
    
    let userMsg = document.createElement("div");
    userMsg.className = "message user";
    userMsg.innerText = "You: " + message;
    chatBox.appendChild(userMsg);
    inputField.value = "";
    
    fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            instruction: message,
            current_draft: draftText.innerText
        })
    })
    .then(res => res.json())
    .then(data => {
        if(data.success) {
            let aiMsg = document.createElement("div");
            aiMsg.className = "message ai";
            aiMsg.innerText = "System: Draft updated.";
            chatBox.appendChild(aiMsg);
            draftText.innerText = data.new_draft;
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    });
}