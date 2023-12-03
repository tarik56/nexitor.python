import time

from flask import Flask, jsonify, request
from nexitor.nexitor_flask import NexitorFlask


app = Flask(__name__, )

NexitorFlask(
    url="asd",
    application="test",
    instance="test",
    api_key="test",
    handler=app
)


@app.route('/', methods=['GET'])
def get_task():
    time.sleep(1)
    return jsonify({'task': "task1"})


@app.route('/tasks', methods=['POST'])
def create_task():
    return jsonify({'task': "task1"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8090, threaded=True, debug=False, use_reloader=False)
