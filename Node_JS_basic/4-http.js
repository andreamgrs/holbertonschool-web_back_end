// import the http module
const http = require('http');

const PORT = 1245;

// create a server, res and req are execute in every request
const app = http.createServer((req, res) => {
  // set the response with status and content type
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  // send the resp body
  res.end('Hello Holberton School!');
});

app.listen(PORT, 'localhost', () => {
  console.log(`App server running at http://localhost:${PORT}/`);
});

module.exports = app;
