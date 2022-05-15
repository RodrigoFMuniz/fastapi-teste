from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'Hello World!'

@app.get('/User')
def new_route():
    return {'data':{'name':'Rodrigo'}}