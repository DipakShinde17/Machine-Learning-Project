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


## 2) 🧠 Resume Screening System (Machine Learning)

This project is a Machine Learning-based Resume Screening System designed to automate the process of shortlisting candidates based on their resumes.

The system uses a trained ML model to analyze resume data and predict whether a candidate is suitable for a specific role. It focuses on structured data processing and classification without using advanced NLP techniques.

The application is deployed using Streamlit, providing a simple and interactive interface for uploading resumes and viewing predictions.

### 🚀 Features:

* Upload resume files for analysis
* ML-based classification of resumes
* Fast and automated candidate screening
* Interactive UI using Streamlit

### 🛠️ Technologies Used:

* Python
* Machine Learning (Scikit-learn)
* Streamlit (Deployment)
* Pandas, NumPy

### 📊 Workflow:

1. Load dataset
2. Preprocess data
3. Train ML model
4. Save model using `.pkl`
5. Use Streamlit app for prediction

## 📂 Project Structure

├── .ipynb_checkpoints/
→ Auto-generated Jupyter backup files (can be ignored)

├── ai_resume_screening.csv
→ Dataset used for training the model

├── command run.txt
→ Contains commands to run the project

├── NLP_demo.py
→ Python script for testing model prediction

├── Project Explanation.docx
→ Documentation of the project

├── requirements.txt
→ List of required Python libraries

├── Resume.ipynb
→ Notebook used for model training

├── resume.py
→ Core logic for prediction

├── resume.pkl
→ Trained Machine Learning model

├── scaler.pkl
→ Data scaling model used before prediction

