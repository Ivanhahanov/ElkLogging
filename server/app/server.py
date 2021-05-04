from flask import Flask, jsonify
import logging
from logstash_async.handler import AsynchronousLogstashHandler

host = 'logstash'
port = 5000
logger = logging.getLogger('simple-app')
logger.setLevel(logging.DEBUG)
async_handler = AsynchronousLogstashHandler(host, port, database_path=None)
logger.addHandler(async_handler)


app = Flask(__name__)


@app.route("/")
def index():
    logger.info("info log")
    return jsonify({"hello": "World"})


@app.route("/bye")
def logout():
    logger.warning("warn log")
    return jsonify({"bye": "World"})


if __name__ == '__main__':
    logger.info("server started")
    app.run(host="0.0.0.0")
