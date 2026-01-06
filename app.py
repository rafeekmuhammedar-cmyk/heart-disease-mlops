from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("logistic_regression_pipeline.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]
        return jsonify({
            "prediction": int(prediction),
            "probability": float(probability)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
