from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Remove and save dominant emotion for formatted output
    dominant = response.pop('dominant_emotion')

    # Return a formatted string with the sentiment label and score
    return f'For the given statement, the system response is {key:val for key,val in response.items()}. The dominant emotion is {dominant}.'

@app.route("/")
def render_index_page():
    return render_template('index.html')@app.route("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

