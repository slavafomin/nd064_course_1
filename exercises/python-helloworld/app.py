
import logging

from flask import Flask


logging.basicConfig(
    format='[%(asctime)s] [%(levelname)s]: %(message)s',
    filename='app.log',
    encoding='utf-8',
    level=logging.DEBUG
)

app = Flask(__name__)


@app.route("/")
def hello():
    logging.debug('Home endpoint reached')
    return "Hello World"


@app.route("/status")
def status():
    logging.debug('Status endpoint reached')
    return {
        "result": "OK"
    }


@app.route("/metrics")
def metrics():
    logging.debug('Metrics endpoint reached')
    return {
        "UserCount": 140,
        "UserCountActive": 23,
    }


if __name__ == "__main__":
    app.run()
