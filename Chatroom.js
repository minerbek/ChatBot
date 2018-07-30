<head>
  <link rel="stylesheet" href="https://npm-scalableminds.s3.eu-central-1.amazonaws.com/@scalableminds/chatroom@master/dist/Chatroom.css" />
</head>
<body>
  <div class="chat-container"></div>

  <script src="https://npm-scalableminds.s3.eu-central-1.amazonaws.com/@scalableminds/chatroom@master/dist/Chatroom.js"/></script>
  <script type="text/javascript">
    var chatroom = window.Chatroom({
      host: "http://localhost:8081",
      title: "Chat with Mike",
      container: document.querySelector(".chat-container"),
      welcomeMessage: "Hi, I am Mike. How may I help you?"
    });
    chatroom.openChat();
  </script>
</body>