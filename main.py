import uvicorn
from api import app

if __name__ == '__main__':
    uvicorn.run(host='0.0.0.0', port=8000, log_level='info', app=app)
