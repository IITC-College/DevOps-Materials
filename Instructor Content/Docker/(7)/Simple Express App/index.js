const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;
const users = [];

app.use(bodyParser.json());

app.get('/', (request, response) => {
  response.send('Hello World');
});

app.post('/users', (request, response) => {
  const userId = request.body.userId;

  if (!userId) {
    response.status(400).send('Missing userId');
    return;
  }

  if (users.includes(userId)) {
    response.status(400).send('User already registered');
    return;
  }

  users.push(userId);
  response.status(201).send('User registered');
});

app.get('/users', (request, response) => {
  response.json({ users });
});

app.listen(port, () => {
  console.log('Server listening on port 3000');
});
