# loan_approval_system


🏦 Loan Approval Prediction Web App
📌 Project Overview

This project is a Machine Learning based web application that predicts whether a loan application will be Approved or Rejected based on user inputs such as income, CIBIL score, assets, etc.

The model is built using Logistic Regression and deployed using a Flask web application.

🚀 Features

Predict loan approval status (Approved / Rejected)

User-friendly input form

Real-time prediction using trained ML model

Simple and lightweight web interface

🧠 Machine Learning Model

Algorithm: Logistic Regression

Type: Classification

Target Variable: loan_status

📊 Input Features:

Number of Dependents

Education

Self Employed

Annual Income

Loan Amount

Loan Term

CIBIL Score

Residential Assets Value

Commercial Assets Value

Luxury Assets Value

Bank Asset Value

🗂️ Project Structure
loan_prediction_project/
│
├── loan_model.pkl        # Trained ML model
├── app.py                # Flask backend
│
├── templates/
│   ├── index.html        # Input form
│   └── result.html       # Prediction result
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone <your-repo-link>
cd loan_prediction_project
2️⃣ Install dependencies
pip install -r requirements.txt

If requirements.txt is not available, install manually:

pip install flask pandas scikit-learn joblib
▶️ Run the Application
python app.py

Open your browser and go to:

http://127.0.0.1:5000
📈 How It Works

User enters details in the form

Data is sent to Flask backend

Backend loads trained model (loan_model.pkl)

Model predicts loan status

Result is displayed on screen

💾 Model Saving

The trained model is saved using:

joblib.dump(model, "loan_model.pkl")

And loaded using:

model = joblib.load("loan_model.pkl")
📌 Future Improvements

Add better UI using CSS & animations

Use dropdowns instead of manual number inputs

Display prediction probability

Deploy on cloud (Render / Heroku)

Add authentication system

👨‍💻 Author

Harshda Patil

⭐ Acknowledgement

This project is built for learning Machine Learning deployment and real-world application development.