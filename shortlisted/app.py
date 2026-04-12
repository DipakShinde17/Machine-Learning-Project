

from flask import Flask, render_template, request
import pdfplumber
import docx

app = Flask(__name__)

# 🔹 Skill variations (SMART MATCHING)
SKILL_MAP = {
    "python": ["python"],
    "java": ["java"],
    "sql": ["sql"],
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "dl"],
    "data analysis": ["data analysis", "data analytics"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "matplotlib": ["matplotlib"],
    "seaborn": ["seaborn"],
    "tensorflow": ["tensorflow"],
    "scikit learn": ["scikit learn", "sklearn"],
    "nlp": ["nlp", "natural language processing"],
    "statistics": ["statistics"],
    "excel": ["excel"],
    "power bi": ["power bi"],
    "tableau": ["tableau"],
    "mysql": ["mysql"]
}

# 🔹 Extract PDF
def extract_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.lower()

# 🔹 Extract DOCX
def extract_docx(file):
    doc = docx.Document(file)
    return " ".join([para.text for para in doc.paragraphs]).lower()

# 🔹 Extract skills (SMART)
def extract_skills(text):
    text = text.lower()
    found = set()

    for skill, variations in SKILL_MAP.items():
        for v in variations:
            if v in text:
                found.add(skill)

    return found

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["resume"]
    job_desc = request.form["job_desc"].lower()

    # 🔹 Resume text extraction
    if file.filename.endswith(".pdf"):
        resume_text = extract_pdf(file)
    elif file.filename.endswith(".docx"):
        resume_text = extract_docx(file)
    else:
        return "Unsupported file format"

    # 🔹 Extract skills
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_desc)

    matched_skills = resume_skills.intersection(jd_skills)

    # 🔹 Score calculation
    if len(jd_skills) == 0:
        score = 0
    else:
        score = (len(matched_skills) / len(jd_skills)) * 100

    print("Resume Skills:", resume_skills)
    print("JD Skills:", jd_skills)
    print("Matched Skills:", matched_skills)
    print("Score:", score)

    # 🔥 FINAL DECISION LOGIC
    if score >= 25 or len(matched_skills) >= 2:
        result = f"Shortlisted ✅ (Score: {score:.2f}%)"
    else:
        result = f"Rejected ❌ (Score: {score:.2f}%)"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)



    # Looking for Python developer with Machine Learning, SQL and Pandas