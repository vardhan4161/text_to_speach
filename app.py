from flask import Flask, render_template, request, jsonify
from agent import SpeechAgent

app = Flask(__name__)
agent = SpeechAgent()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({
            "status": "error",
            "message": "No text provided.",
            "audio_path": None
        }), 400
    
    lang = data.get('lang', 'en')
    gender = data.get('gender', 'Female')
    
    response = agent.run(data['text'], lang=lang, gender=gender)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
