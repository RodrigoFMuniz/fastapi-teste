from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    print('Index function')
    return 'Hello World!'
    # return 'olá ' * (1+1)

@app.get('/user')
def new_route():
    print('new_route function')
    return {'data':{'name':'Rodrigo'}}

@app.get('/about')
def about():
    return 'About page'

@app.get('/rota/{id}')
def param_route(id):
    return {'Id':id}