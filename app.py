from flask import Flask, request, jsonify
import cv2

app = Flask(__name__)

@app.route('/')
def home():
    return "Age & Gender Detection API Running"

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    filepath = "temp.jpg"
    file.save(filepath)

    # Dummy response (replace with your detect.py logic)
    return jsonify({
        "gender": "Male",
        "age": "25-32"
    })

if __name__ == '__main__':
    app.run()