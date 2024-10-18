var socket = io('http://192.168.1.111:5000');

document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('form');
    var input = document.getElementById('message-input');
    var messages = document.getElementById('messages');
    var nicknameInput = document.getElementById('nickname-input');
    var startChatButton = document.getElementById('start-chat');
    var loginContainer = document.getElementById('login-container');
    var chatInterface = document.getElementById('chat-interface');
    var nickname = '';

    startChatButton.onclick = function() {
        nickname = nicknameInput.value.trim();
        if (nickname) {
            loginContainer.style.display = 'none';
            chatInterface.style.display = 'flex';
        }
    };

    form.onsubmit = function(e) {
        e.preventDefault();
        var message = input.value;
        if (message.trim()) {
            socket.send({ nickname: nickname, message: message, type: 'sent' });
            input.value = '';
        }
        return false;
    };

    socket.on('message', function(data) {
        var item = document.createElement('li');
        if (data.type === 'sent') {
            item.classList.add('sent');
        } else {
            item.classList.add('received');
        }
        item.textContent = `${data.nickname}: ${data.message}`;
        messages.appendChild(item);
        window.scrollTo(0, document.body.scrollHeight);
    });
});
