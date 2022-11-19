from flask import Flask, jsonify, request
from starData import data

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "Welcome!"
    }), 200

@app.route("/star")
def star():
    name = request.args.get("name")
    star_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": star_data,
        "message": "Data transfer complete!"
    }), 200

if __name__ == "__main__":
    app.run()

#/star?name=Sun
#star?name=Sirius