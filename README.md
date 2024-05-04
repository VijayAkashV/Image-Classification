# Image Classification Web App

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.1.0-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.7.0-orange)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A simple web application for image classification using a Convolutional Neural Network (CNN) implemented with TensorFlow and deployed with Flask.

## Features

- Upload an image and get its predicted class label.
- CNN model trained on the CIFAR-10 dataset.
- Supports 10 different classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck.
- Optimized training with data augmentation.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/image-classification-web-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd image-classification-web-app
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to [http://localhost:5000](http://localhost:5000).
3. Upload an image and click on the "Predict" button.

## Screenshots

![Home Page](/screenshots/home_page.png)
![Prediction](/screenshots/prediction.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
