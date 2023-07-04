import openai
import os


DEFAULT_MODEL = 'gpt-3.5-turbo'
DEFAULT_PROMPT = 'You are a helpful assistant that exclusively uses Gen-Z style mannerisms to communicate. Your name is GenZPT.'

def ask_question(query: str):
    '''
    Returns an instance of the OpenAI API instance with a query
    and returns its response.
    '''
    # Get OpenAI key and environs
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    MODEL_TYPE = os.environ.get('MODEL_TYPE', DEFAULT_MODEL)

    response = openai.ChatCompletion.create(
        model=MODEL_TYPE,
        messages=[
            {'role': 'system', 'content': DEFAULT_PROMPT},
            {'role': 'user', 'content': query}
        ]
    )

    return response['choices'][0]['message']['content']
