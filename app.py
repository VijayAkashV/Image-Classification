from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

# Load the trained model
model = load_model('cnn_model.h5')

# Map model predictions to class labels
class_labels = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

# Directory to save uploaded images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Render the home page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction function
def predict(image):
    img = Image.open(image)
    img = img.resize((32, 32))
    img = np.expand_dims(img, axis=0)
    img = np.array(img)/255.0
    result = model.predict(img)
    predicted_class = np.argmax(result)
    return class_labels[predicted_class], img

# Handle image upload and prediction
@app.route('/predict', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Save the uploaded image
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(image_path)
            
            # Make prediction
            prediction, img = predict(image_path)
            
            return render_template('index.html', prediction=prediction, img_path=file.filename)
    return render_template('index.html', prediction="Prediction failed!")

if __name__ == '__main__':
    app.run(debug=True)
