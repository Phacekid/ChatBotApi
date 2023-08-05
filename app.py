from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
from appFunctions import conversation

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hi there"

@app.route('/chat', methods=['POST'])
def chat():
    content_type = request.headers.get('Content-Type')
    prompt = None
    if (content_type == 'application/json'):
        json_payload = request.json
        prompt = json_payload['question']
    else:
        return 'Content-Type not supported!'
    
    result = conversation(prompt)
    
    # if you want to store your chat history, you can enable this block of code
    # file_path = "memory.txt"
    # with open(file_path, "w") as file:
    #     file.write(str(result['chat_history']))
    
    return {
        'statusCode': 200,
        'question': result['question'],
        'answer':  result['answer'],
    }

if __name__ == "__main__":
    app.run("0.0.0.0")