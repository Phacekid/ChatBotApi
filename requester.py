#format to make POST request to api endpoints

import requests

url = 'http://127.0.0.1:5000/chat'
headers = {
    'Content-Type': 'application/json'
}
# # if youre making a request to a retrieval_qa.py flask app
# data = {
#     'prompt': 'Hello?'
# }

# if youre making a request to a conv_retrieval.py flask app
# Note that dictionary key changed from prompt to question

data = {
    'question': 'Hello?'
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    json_response = response.json()
    print(json_response['answer'])
else:
    print(f"Request failed")
