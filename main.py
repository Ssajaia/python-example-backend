from flask import Flask, Response

app = Flask(__name__)


@app.get("/")
def home():
    return Response("welcome to the Flask API!", mimetype="text/plain")


@app.get("/hello")
def hello():
    return Response("Hello, World!", mimetype="text/plain")


@app.get("/status")
def status():
    return Response("OK", mimetype="text/plain")


@app.get("/health")
def health():
    return Response("Healthy", mimetype="text/plain")


@app.get("/version")
def version():
    return Response("1.0.0", mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)