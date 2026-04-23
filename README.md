# 🫁 Pneumonia Detection System using Deep Learning

## 📌 Overview

This project is a **deep learning-based web application** that detects **pneumonia from chest X-ray images**.
It uses a trained Convolutional Neural Network (CNN) model and provides predictions through a user-friendly web interface built with Flask.

The system also includes **heatmap visualization** to highlight the regions influencing the model’s decision, improving interpretability.

---

## 🚀 Features

* 📤 Upload chest X-ray images
* 🤖 Predict **Normal** or **Pneumonia**
* 📊 Confidence score display
* 🔥 Heatmap visualization (model interpretability)
* 🌐 Simple and clean web interface

---

## 🖥️ Application Demo

### 🔹 Upload & Prediction Interface

![Upload](screenshots/upload.png)

---

### 🔹 Normal Prediction Result

![Normal](screenshots/normal.png)

---

### 🔹 Pneumonia Detection Result

![Pneumonia](screenshots/pneumonia.png)

---

### 🔹 Dataset Samples (Training)

![Dataset](screenshots/dataset.png)

---

### 🔹 Heatmap Visualization

![Heatmap](screenshots/heatmap.png)

---

## 🧠 Model Details

* Model Type: **Convolutional Neural Network (CNN)**
* Framework: **TensorFlow / Keras**
* Input: Chest X-ray images
* Output: Binary classification (**Normal / Pneumonia**)

---

## ⚙️ Tech Stack

* **Python**
* **TensorFlow / Keras**
* **Flask**
* **HTML / CSS**
* **NumPy / OpenCV / Matplotlib**

---

## 📂 Project Structure

```
MedicalProject/
│── app.py
│── templates/
│   └── index.html
│── static/
│   └── (images, outputs, heatmaps)
│── FinalModel.ipynb
│── screenshots/
│── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Medicalproject.git
cd Medicalproject
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask app

```bash
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Results

* Successfully classifies chest X-rays into **Normal** and **Pneumonia**
* Provides **confidence scores**
* Generates **heatmaps** for explainability

---

## 🎯 Future Improvements

* Improve model accuracy with larger datasets
* Deploy the application (Render / Heroku)
* Add multi-class classification (viral vs bacterial pneumonia)
* Enhance UI/UX

---

## 🙌 Acknowledgement

Dataset used: Chest X-ray dataset for pneumonia detection
Libraries: TensorFlow, Keras, Flask, OpenCV


