from flask import Flask, request
from flask_cors import CORS
from retrievalQaFunction import questions
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hi there!"

@app.route('/chat', methods=['POST'])
def chat():
    content_type = request.headers.get('Content-Type')
    prompt = None
    if (content_type == 'application/json'):
        json_payload = request.json
        prompt = json_payload['prompt']
    else:
        return 'Content-Type not supported!'
    
    result = questions(prompt)
    return {
        'statusCode': 200,
        'question': result['query'],
        'answer':  result['result']
    }


if __name__ == "__main__":
    app.run("0.0.0.0")