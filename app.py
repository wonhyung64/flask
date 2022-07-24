from flask import Flask, jsonify

count = 0

app = Flask(__name__)


@app.route("/")
def home():
    global count
    count += 1
    return jsonify(
	text="Hello, world",
	count = count
    )

