from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_task():
    task = request.args.get('task')
    if not task:
        return jsonify({"error": "No task provided"}), 400
    # Save the task into a file
    with open(f"/tasks/{task}.txt", "w") as f:
        f.write(f"Task {task} executed.")
    return jsonify({"message": f"Task {task} executed."}), 200

@app.route('/read', methods=['GET'])
def read_file():
    path = request.args.get('path')
    if not path:
        return jsonify({"error": "No path provided"}), 400
    # Read the file content
    if not os.path.exists(path):
        return jsonify({"error": "File not found"}), 404
    with open(path, 'r') as f:
        content = f.read()
    return jsonify({"content": content}), 200

if __name__ == '__main__':
    os.makedirs('/tasks', exist_ok=True)  # Make sure the /tasks folder exists
    app.run(host='0.0.0.0', port=8000)
