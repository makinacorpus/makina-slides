var fs = require('fs'), http = require('http');

http.createServer(function (req, res) {
  fs.readFile(__dirname + req.url, function (err, data) {
    res.writeHead(200);
    setTimeout(function() {  // Délai artificiel pour la démo
      res.end(data);
    }, 2000);
  });
}).listen(8080);
