from fastapi import FastAPI
from sql_app.schemas import Blog
from sql_app import models, schemas
from sql_app.db import engine

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.post('/blog')
def create(request: Blog):
    return request

# @app.post('/blog')
# def create(title, body):
#     return {'title':title, 'body':body }
