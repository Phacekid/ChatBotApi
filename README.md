# ChatBotApi

Langchain OpenAI Chat Bot with Api endpoint for FLASK app using POST requests.

### Setup

To know more on setup please check [ChatBot](https://github.com/Phacekid/ChatBot)

### Sources

- [Code an OpenAI integration with Python and Flask](https://www.youtube.com/watch?v=Vo1_9-qVCM4&t=412s)

### Tips

- The previous [ChatBot](https://github.com/Phacekid/ChatBot) was a gradio app to chat with your data but now you can also create an API endpoint for your chatbot and integrate it to any app of your choice by simply making post requests.
- Don't forget to run `pip install -r requirements.txt`

### NOTE

There are some python files and their respective functions are:

- _app.py_: main flask app that uses ConversationalRetrievalChain in _appFunctions.py_ for the chatting over your documents.
- _requester.py_: a demo python code that shows how to make post request to the api endpoint.
- _retrievalQa.py_: another flask app that uses RetrievalQA for question and answer over your documents, some of its functions are imported from _retrievalQaFunction.py_

### APP RUN

- use `flask run` to run the _app.py_

- if you want to run the _retrievalQa.py_, since you'll most likely be using either retrieval or conversation, you can rename it to be app.py, then use `flask run`

### Pending

- [ ] same as [ChatBot](https://github.com/Phacekid/ChatBot)
