"""
Emotion Detection Server Module

This module contains the Flask web server for the Emotion Detection application.
It provides routes for the home page and the emotion detection API.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the home page.

    Returns:
        HTML: Rendered HTML page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Detect emotion from the provided text.

    Returns:
        JSON: A JSON response with emotion scores and dominant emotion.
    """
    data = request.get_json()
    text = data.get('text', '')
    result = emotion_detector(text)
    if result['dominant_emotion'] is None:
        return jsonify({'error': 'Invalid text! Please try again!'}), 400
    response = {
        'anger': result['anger'],
        'disgust': result['disgust'],
        'fear': result['fear'],
        'joy': result['joy'],
        'sadness': result['sadness'],
        'dominant_emotion': result['dominant_emotion']
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
