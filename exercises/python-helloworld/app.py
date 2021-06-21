from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/status")
def status():
    return {
        "result": "OK — Healthy"
    }


@app.route("/metrics")
def metrics():
    return {
        "UserCount": 140,
        "UserCountActive": 23,
    }


if __name__ == "__main__":
    app.run()
