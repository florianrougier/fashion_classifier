#Stage 1: Import all project dependencies
import os
import requests
import numpy as np
import tensorflow as tf

from imageio import imwrite, imread
from flask import Flask, request, jsonify, render_template

# Stage 2: Load the pretrained model

# Loading the model structure
with open("fashion_model_flask.json", 'r') as f:
    model_json = f.read()

model = tf.keras.models.model_from_json(model_json)
  

# Loading model weights
model.load_weights("fashion_model_flask.h5")

# Stage 3: Create the Flask API
# Defining the Flask app
app = Flask(__name__)

#Defining a default route:
@app.route("/", methods=["GET"])
def home():
    return render_template('home.html')

# Defining the classify_image function
@app.route("/api/v1/<string:img_name>", methods=["POST"])
def classify_image(img_name):
    
    upload_dir = "uploads/"

    image = imread(upload_dir + img_name)
    
    classes = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
    
    prediction = model.predict([image.reshape(1, 28 *28)])
    
    
    return jsonify({"object_detected":classes[np.argmax(prediction[0])],
                    "confidence": "%.3f" % np.max(prediction[0])})

# Start the Flask API and make predictions
app.run(port=5000, debug=False)    