var app = require('express')();
var http = require('http').createServer(app);
var io = require('socket.io')(http);

const port = 8000;


app.get('/', function(req, res){
  res.sendFile(__dirname + '/Client.html');
});

io.on('connection', function(socket){
    console.log('a user connected');
    socket.on('message', function (data) {
    console.log(data);
    io.sockets.emit('new message',data);
    });
    socket.on('disconnect', function(){
      console.log('user disconnected');
    });
  });

http.listen(port, function(){
  console.log(`listening on *:${port}`);
});