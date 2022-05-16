from fastapi import FastAPI
from sql_app.schemas import Blog

app = FastAPI()

@app.post('/blog')
def create(request: Blog):
    return request

# @app.post('/blog')
# def create(title, body):
#     return {'title':title, 'body':body }