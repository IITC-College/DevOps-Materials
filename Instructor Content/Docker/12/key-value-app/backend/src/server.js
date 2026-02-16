const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT;

app.use(bodyParser.json());

mongoose.connect(`mongodb://${process.env.MONGODB_HOST}/${process.env.KEY_VALUE_DB}`,
    {
        auth: {
            username: process.env.KEY_VALUE_USER,
            password: process.env.KEY_VALUE_PASSWORD
        },
        connectTimeoutMS: 500
    }
).then(() => {
    console.log('MongoDB connected successfully');
    app.listen(PORT, () => {
        console.log(`Server listening on port ${PORT}`);
    });
}).catch((err) => {
    console.error('Something went wrong');
    console.error(err);
    process.exit(1);
});

app.get('/health', (req, res) => {
    res.json({ ok: true, message: 'Health check!!' });
});