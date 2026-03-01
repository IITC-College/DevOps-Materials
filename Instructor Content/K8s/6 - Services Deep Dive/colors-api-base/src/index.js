const express = require('express');

const port = 80;
const app = express();

app.get('/', (req, res) => {
  res.send('<h1 style="color:blue;">Hello from Color API!</h1>');
});

app.listen(port, () => {
  console.log(`Color API listening on port: ${port}`);
});