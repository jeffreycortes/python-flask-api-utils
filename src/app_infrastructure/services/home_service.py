from .app import app, jsonify

@app.route("/")
def index():
    return jsonify('Hello from Index')

@app.route("/api")
def indexAPI():
    return jsonify('Hello from API')
