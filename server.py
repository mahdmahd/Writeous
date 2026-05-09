from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

active_writers = {}

@app.route('/universe')
def universe():
    return render_template('cat.html')

@app.route('/heartbeat', methods=['POST'])
def heartbeat():
    data = request.json
    writer_id = data.get("writer", "Anonymous")
    active_writers[writer_id] = time.time()
    print(f"✨ Heartbeat from {writer_id}")
    return jsonify({"status": "received"})

@app.route('/get-pulses', methods=['GET'])
def get_pulses():
    now = time.time()
    # Return a list of writers who have saved in the last 5 minutes
    writing_now = [
        writer for writer, last_time in active_writers.items()
        if (now - last_time) < 300
    ]
    return jsonify({"active_writers": writing_now})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
