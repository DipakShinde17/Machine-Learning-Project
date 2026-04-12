from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("resume_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    years_experience = float(request.form["years_experience"])
    skills_match_score = float(request.form["skills_match_score"])
    education_level = int(request.form["education_level"])
    project_count = int(request.form["project_count"])
    resume_length = float(request.form["resume_length"])
    github_activity = float(request.form["github_activity"])

    input_data = np.array([[ 
        years_experience,
        skills_match_score,
        education_level,
        project_count,
        resume_length,
        github_activity
    ]])

    prediction = model.predict(input_data)

    result = "Shortlisted ✅" if prediction[0] == 1 else "Rejected ❌"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
