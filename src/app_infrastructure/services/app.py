#flask
from flask import Flask, jsonify, request
from flask_cors import CORS

# creating the Flask application
app = Flask(__name__)
CORS(app)
