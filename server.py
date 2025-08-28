"""Flask server for the Emotion Detection App.

This module starts a Flask web server to serve the emotion detection
application. It provides routes for rendering the main page and for
processing emotion detection requests.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def render_index_page():
    """Render the main index page of the application."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def analyze_emotion():
    """Analyze the provided text and return the detected emotions.

    Returns:
        str: A formatted response containing the emotion scores and the
        dominant emotion, or an error message if the text is invalid.
    """
    text_to_analyze = request.args.get("textToAnalyze", default="", type=str)
    response = emotion_detector(text_to_analyze)

    if not response or response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
