import argparse
import base64
import os
from pathlib import Path
from io import BytesIO
import time
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
print("Welcome to the Imaginarium Server. This might take up to two minutes.")

parser = argparse.ArgumentParser(description = "Imaginarium app to visualize prompts")
parser.add_argument("--port", type=int, default=8000, help = "backend port")

args = parser.parse_args()

@app.route("/ping", methods=["GET"])
@cross_origin()
def ping():
    return "pong"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=args.port, debug=False)
