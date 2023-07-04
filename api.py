from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from ai import ask_question


app = FastAPI()

# Serve frontend
app.mount('/static', StaticFiles(directory='static'), name='static')

'''
    POST - Send message
'''

class NewMessage(BaseModel):
    '''
    Represents an incoming message.
    '''
    message: str


@app.post('/api/speak')
def speak_message(body: NewMessage):
    '''
    Receives a new message.
    '''
    message = body.message
    response = ask_question(message)
    return {'response': response}
