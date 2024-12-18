from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Sandbox!"

@app.route('/api/example', methods=['GET'])
def example():
    return jsonify({"message": "This is a sandboxed API response!"})

@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({"message": f"Hello, {name}! Welcome to the sandbox."})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
