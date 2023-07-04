document.getElementById('chat-form').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent form submission

  var messageInput = document.querySelector('#message-input');
  var messageText = messageInput.value.trim();

  if (messageText !== '') {
    addMessage('You', messageText);
    sendMessage(messageText).then(
      (res) => {
        addMessage('GenZ-PT', res);
      },
      (rej) => addMessage('Error', 'Failed to send'));
    messageInput.value = '';
    messageInput.focus();
  }
});

function addMessage(user, text) {
  var chatBody = document.getElementById('chat-body');
  var messageDiv = document.createElement('div');
  messageDiv.className = 'message';
  messageDiv.innerHTML = '<div class="user">' + user + '</div><div class="text">' + text + '</div>';
  chatBody.appendChild(messageDiv);
  chatBody.scrollTop = chatBody.scrollHeight;
}

async function sendMessage(messageContent) {
  // Sends a message to the OpenAI API
  const body = {
    message: messageContent
  }

  const response = await fetch('/api/speak', {
      method: 'POST',
      cache: 'no-cache',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(body)
    });

  const parsed = await response.json();
  return parsed.response
}
