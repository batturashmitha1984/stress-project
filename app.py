from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]
    prediction = model.predict([data])
    return jsonify({"stress_level": int(prediction[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)