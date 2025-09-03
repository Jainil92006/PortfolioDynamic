function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (!message) return;

    appendMessage("You", message, "user");
    input.value = "";

    fetch("/get", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ msg: message })
    })
    .then(response => response.json())
    .then(data => {
        appendMessage("Bot", data.response, "bot");
    });
}

function appendMessage(sender, message, cls) {
    const chatbox = document.getElementById("chat-box");
    const newMessage = document.createElement("p");
    newMessage.className = cls;
    newMessage.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatbox.appendChild(newMessage);
    chatbox.scrollTop = chatbox.scrollHeight;
}







