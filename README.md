# stress-detector-app
# 🧠 Stress Level Prediction Web App

A full-stack Machine Learning web application that predicts stress levels based on user inputs like age, sleep hours, and work hours. Built using Flask, Docker, and a simple web UI.

---

## 🚀 Features
- Real-time stress level prediction
- Machine Learning model (Scikit-learn)
- Flask REST API backend
- Docker containerized application
- HTML/CSS/JavaScript frontend
- Ready for cloud deployment (AWS)

---

## 🛠️ Tech Stack
- Python
- Flask
- Scikit-learn
- HTML, CSS, JavaScript
- Docker
- Git & GitHub

---

## 📂 Project Structure

stress-project/
│
├── app.py
├── model.pkl
├── Dockerfile
├── requirements.txt
├── README.md
│
├── templates/
│     └── index.html
│
└── static/
      └── style.css

---

## ⚙️ How to Run Locally

### 1. Clone repository
git clone https://github.com/batturashmitha1984/stress-project.git
cd stress-project

### 2. Build Docker image
docker build -t stress-app .

### 3. Run container
docker run -p 5001:5001 stress-app

### 4. Open in browser
http://127.0.0.1:5001

---

## 📊 Model Information
- Algorithm: Random Forest / Decision Tree
- Inputs:
  - Age
  - Sleep Hours
  - Work Hours
- Output:
  - 0 = Low Stress 😊
  - 1 = Medium Stress 😐
  - 2 = High Stress 😣

---

## 🌟 Future Improvements
- Deploy on AWS EC2
- Add database to store predictions
- Improve UI with charts
- Add authentication system

---

## 👨‍💻 Author
- Rashmitha 
- GitHub: https://github.com/batturashmitha1984
