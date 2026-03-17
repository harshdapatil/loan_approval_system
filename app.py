from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("loan_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = {
        "no_of_dependents": int(request.form["dependents"]),
        "education": int(request.form["education"]),
        "self_employed": int(request.form["self_employed"]),
        "income_annum": int(request.form["income"]),
        "loan_amount": int(request.form["loan_amount"]),
        "loan_term": int(request.form["loan_term"]),
        "cibil_score": int(request.form["cibil"]),
        "residential_assets_value": int(request.form["res_assets"]),
        "commercial_assets_value": int(request.form["com_assets"]),
        "luxury_assets_value": int(request.form["lux_assets"]),
        "bank_asset_value": int(request.form["bank_assets"])
    }

    sample = pd.DataFrame([data])

    prediction = model.predict(sample)

    if prediction[0] == 1:
        result = "Loan Approved ✅"
    else:
        result = "Loan Rejected ❌"

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)