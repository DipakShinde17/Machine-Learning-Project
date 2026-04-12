## 1) 🧠 Shortlisting System

The Resume Shortlisting System is a Machine Learning-based web application designed to automate the process of screening resumes. The system analyzes resumes and matches them against job requirements using Natural Language Processing (NLP) techniques.

It helps recruiters quickly identify the most relevant candidates by evaluating skills, keywords, and experience mentioned in resumes.

The application integrates a trained ML model with a user-friendly web interface, enabling efficient and accurate resume filtering.

### 🚀 Features:

* Upload and analyze resumes
* Keyword-based and NLP-based matching
* Automated candidate shortlisting
* Simple web interface for interaction

### 🛠️ Technologies Used:

* Python
* Machine Learning (Scikit-learn)
* Natural Language Processing (NLP)
* Flask (Web Framework)

## 📂 Project Structure

├── **pycache**/
→ Stores compiled Python files (auto-generated, not important)

├── data/
→ Contains datasets used for training/testing the model

├── notebook/
→ Jupyter notebooks used for model training and experimentation

├── static/
→ Stores static files like CSS, JavaScript, images for frontend

├── templates/
→ HTML files used in Flask web application

├── app1.py
→ Main Flask application file (runs the web app and handles routes)

├── nlp_utils.py
→ Contains NLP-related functions like text preprocessing, keyword extraction

├── resume_model.pkl
→ Trained Machine Learning model used for resume classification/shortlisting
