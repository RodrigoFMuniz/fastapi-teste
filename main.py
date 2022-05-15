from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    print('Index function')
    return 'Hello World!'
    # return 'olá ' * (1+1)

@app.get('/blog')
def new_route():
    print('new_route function')
    return {'data':{'name':'Rodrigo'}}

@app.get('/query-blog')
def new_route2(limit):
    print('new_route function')
    return {'data':f'{limit} blogs do DB'}

@app.get('/about')
def about():
    return 'About page'

@app.get('/blog/unpublished')
def unpublished():
    return {f'data':'all unpublished'}

@app.get('/blog/{id}')
def param_route(id):
    return {'Id':id}

@app.get('/blog/{id}/comment')
def comments(id):
    return {f'comment {id}':f'Comentários do id {id}'}
    
@app.get('/blog/{id}/content')
def contents(id: int):
    return {f'content {id}':id}
    
@app.get('/blog/{id}/images')
def images(id: int):
    return {f'images {id}':id}
    