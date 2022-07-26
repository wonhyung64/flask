from flask_cors import CORS
from flask import Flask, jsonify

count = 0

app = Flask(__name__)
cors = CORS(app)

@app.route("/", methods=["GET"])
def home():
    global count
    count += 1
    response = jsonify(
	text="Hello, world",
	count = count
    )
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

