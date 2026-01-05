from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="OK", module="infotainment")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route("/info")
def info():
    return jsonify(module="infotainment", version="1.0.0")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
