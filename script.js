document.getElementById('send-button').onclick = function() {
    const input = document.getElementById('message-input');
    const message = input.value;
    input.value = '';

    fetch('/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
    });
};

function loadMessages() {
    fetch('/messages')
        .then(response => response.json())
        .then(data => {
            const chatBox = document.getElementById('chat-box');
            chatBox.innerHTML = data.messages.map(msg => `<div>${msg}</div>`).join('');
            chatBox.scrollTop = chatBox.scrollHeight;
        });
}

setInterval(loadMessages, 1000);
