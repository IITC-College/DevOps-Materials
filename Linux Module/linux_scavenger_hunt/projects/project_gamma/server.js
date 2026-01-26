const express = require('express');
const mongoose = require('mongoose');
const Bull = require('bull');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(express.json());

// Database connection
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost:27017/gamma', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

// Job queue setup
const analyticsQueue = new Bull('analytics', {
  redis: {
    host: process.env.REDIS_HOST || 'localhost',
    port: process.env.REDIS_PORT || 6379
  }
});

// Routes
app.get('/', (req, res) => {
  res.json({
    service: 'Project Gamma',
    version: '3.0.1',
    status: 'operational'
  });
});

app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    database: mongoose.connection.readyState === 1 ? 'connected' : 'disconnected',
    timestamp: new Date().toISOString()
  });
});

app.post('/api/analytics/job', async (req, res) => {
  const job = await analyticsQueue.add(req.body);
  res.json({ jobId: job.id, status: 'queued' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Project Gamma running on port ${PORT}`);
});

module.exports = app;
