#!/usr/bin/env python3
"""
Project Alpha - Main Application
"""

from flask import Flask, jsonify, request
import yaml
import logging

app = Flask(__name__)

# Load configuration
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Setup logging
logging.basicConfig(
    level=config['logging']['level'],
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return jsonify({
        'app': config['app']['name'],
        'version': config['app']['version'],
        'status': 'running'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/api/users', methods=['GET'])
def get_users():
    # Placeholder for user retrieval
    return jsonify({'users': []})

if __name__ == '__main__':
    logger.info(f"Starting {config['app']['name']}")
    app.run(
        host=config['server']['host'],
        port=config['server']['port'],
        debug=config['app']['debug']
    )
