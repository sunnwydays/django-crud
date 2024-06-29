let message_timeout = document.getElementById("message-timer")

if (message_timeout) {
    setTimeout(() => {
        message_timeout.style.display = "none";
    }, 3000)
}