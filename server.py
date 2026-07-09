from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    # Get text from URL query param
    text_to_analyze = request.args.get('textToAnalyze')

    # Call emotion detector function
    result = emotion_detector(text_to_analyze)

    # Extract scores
    anger_score      = result['anger']
    disgust_score    = result['disgust']
    fear_score       = result['fear']
    joy_score        = result['joy']
    sadness_score    = result['sadness']
    dominant_emotion = result['dominant_emotion']

    # Format and RETURN the response string
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, "
        f"'disgust': {disgust_score}, "
        f"'fear': {fear_score}, "
        f"'joy': {joy_score} and "
        f"'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)