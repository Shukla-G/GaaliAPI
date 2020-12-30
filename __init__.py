from flask import Flask
from flask import jsonify
import random
app = Flask(__name__)
@app.route("/")
def welcome():
    return "Endpoints: /gaali"
@app.route('/gaali', methods=['GET'])
def sendgaali():
    a = ["Bhosdike", "Madarchod", "Bhadhve", "Bhenchod", "Betichod", "Lawde", "Hijre", "Randi"]
    return jsonify({ "gaali": random.choice(a) })

if __name__ == "__main__":
    app.run()
