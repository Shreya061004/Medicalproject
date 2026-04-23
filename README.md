# 🫁 Pneumonia Detection System

## 📌 Overview

This project is a **deep learning-based web application** that detects pneumonia from chest X-ray images.
It uses a Convolutional Neural Network (CNN) model built with TensorFlow/Keras and is deployed using Flask for an interactive user interface.

The system predicts whether a given X-ray image is **Normal** or **Pneumonia** and provides a confidence score for the prediction.

---

## 🚀 Features

* Upload chest X-ray images through a web interface
* Predict **Normal / Pneumonia**
* Display prediction with confidence score
* Simple and user-friendly UI
* End-to-end pipeline: preprocessing → prediction → output

---

## 🧠 Model Details

* Model Type: **Convolutional Neural Network (CNN)**
* Framework: **TensorFlow / Keras**
* Input: Chest X-ray images
* Output: Binary classification (**Normal / Pneumonia**)

---

## ⚙️ Tech Stack

* Python
* TensorFlow / Keras
* Flask
* HTML / CSS
* NumPy / OpenCV

---

## 📂 Project Structure

```
MedicalProject/
│── app.py
│── templates/
│   └── index.html
│── static/
│── FinalModel.ipynb
│── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/your-username/Medicalproject.git
cd Medicalproject
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Results

* Successfully classifies chest X-ray images
* Provides reliable predictions for pneumonia detection
* Can be used as a basic medical decision-support tool

---

## 🎯 Future Improvements

* Improve model accuracy with larger datasets
* Add heatmap/Grad-CAM visualization
* Deploy the application online
* Enhance UI/UX

---

## 👩‍💻 Author

**Shreya Gupta**
GitHub: https://github.com/Shreya061004

---

⭐ If you found this project useful, consider giving it a star!
