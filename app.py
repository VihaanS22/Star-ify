from flask import Flask, jsonify, request
from app_data import data

app = Flask(__name__)

@app.route("/")

def index():
    return jsonify({

        "data" : data,
        "msg" : "SUCCESS"


    }, 200)

@app.route("/star")

def star():
    name = request.args.get("star_name")
    star_data = next(item for item in data if item["star_name"] == name)
    
    return jsonify({

        "data" : star_data,
        "msg" : "SUCCESS"


    }, 200)

if(__name__ == "__main__"):
    app.run()


