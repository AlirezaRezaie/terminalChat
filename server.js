const io = require("socket.io")(process.env.PORT);
console.log("*running on port 3000")
//esablishing connection
io.on("connection", (socket) => {
  console.log("someone connected");

  //broadcasting join message to anyone else in the room
  socket.on("clientJoined", (event) => {
    socket.broadcast.emit("clientJoined", event);
  });

  //broadcasting user messages to another
  socket.on("message", (message) => {
    socket.broadcast.emit("success", { ...message, clientMessage: true });
    //this event is the same as messageSent event
    socket.emit("success", {});
  });

  //broadcasting leave messages to everyone
  socket.on("disconnection", (e) => {
    //in client side this will be called and print's "client_name leaved"
    socket.broadcast.emit("clientLeaved", { ...e });
  });

  //this event redirect's the user to input function (success event)
  socket.on("successHandler", () => {
    socket.emit("success", {});
  });
});
