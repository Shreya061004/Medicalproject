from flask import Flask, render_template, request
import os
from datetime import datetime
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = load_model("finalmodel.h5", compile=False)

# Create static folder if not exists
if not os.path.exists("static"):
    os.makedirs("static")

# ✅ REAL prediction function
def predict_image(filepath):
    img = cv2.imread(filepath)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.reshape(img, (1, 224, 224, 3))

    pred = model.predict(img)[0][0]

    if pred > 0.5:
        result = "PNEUMONIA"
        confidence = pred * 100
    else:
        result = "NORMAL"
        confidence = (1 - pred) * 100

    return result, round(confidence, 2)

# 🔥 Heatmap generator (same as yours)
def generate_heatmap(filename):
    filepath = os.path.join("static", filename)
    original_img = cv2.imread(filepath)

    heatmap = np.random.randint(0, 256,
                                (original_img.shape[0], original_img.shape[1]),
                                dtype=np.uint8)

    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    overlay = cv2.addWeighted(original_img, 0.6, heatmap, 0.4, 0)

    heatmap_filename = f"heatmap_{filename}"
    cv2.imwrite(os.path.join("static", heatmap_filename), overlay)

    return heatmap_filename

# Home route
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    confidence = None
    filename = None
    heatmap_filename = None

    if request.method == "POST":
        file = request.files.get("file")

        if file:
            # Save file
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"{timestamp}_{file.filename}"
            filepath = os.path.join("static", filename)
            file.save(filepath)

            # ✅ REAL prediction
            result, confidence = predict_image(filepath)

            # Heatmap
            heatmap_filename = generate_heatmap(filename)

    return render_template("index.html",
                           result=result,
                           confidence=confidence,
                           filename=filename,
                           heatmap_filename=heatmap_filename)

# Run app
if __name__ == "__main__":
    app.run(debug=True)