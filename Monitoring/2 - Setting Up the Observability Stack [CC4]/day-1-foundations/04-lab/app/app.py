#!/usr/bin/env python3

from flask import Flask, request
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
import time
import os

app = Flask(__name__)

# Prometheus metrics
http_requests_total = Counter(
    'flask_http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

http_request_duration_seconds = Histogram(
    'flask_http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint']
)

# Gauge for monitoring
active_requests = Gauge(
    'flask_active_requests',
    'Active HTTP requests'
)

@app.before_request
def before_request():
    active_requests.inc()
    request.start_time = time.time()

@app.after_request
def after_request(response):
    active_requests.dec()
    duration = time.time() - request.start_time
    http_request_duration_seconds.labels(
        method=request.method,
        endpoint=request.endpoint or 'unknown'
    ).observe(duration)
    http_requests_total.labels(
        method=request.method,
        endpoint=request.endpoint or 'unknown',
        status=response.status_code
    ).inc()
    return response

@app.route('/')
def index():
    return 'Hello from Flask! This is the monitoring lab.', 200

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/slow')
def slow():
    # Simulate slow endpoint (5 seconds)
    time.sleep(5)
    return 'This was slow!', 200

@app.route('/cpu-heavy')
def cpu_heavy():
    # CPU intensive task
    start = time.time()
    while time.time() - start < 10:
        _ = sum(i*i for i in range(100000))
    return 'CPU heavy task done!', 200

@app.route('/memory-leak')
def memory_leak():
    # Simulate memory leak (allocate 100MB and keep it)
    _ = [0] * (10 * 1024 * 1024)  # ~100MB
    return 'Memory allocated!', 200

@app.route('/error')
def error():
    return 'Internal Server Error!', 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
