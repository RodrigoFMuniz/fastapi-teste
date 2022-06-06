from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randint

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [
    {"title":"title of post 1", "content": "Content of post 1","id":1},
    {"title":"title of post 2", "content": "Content of post 2","id":2},
    {"title":"title of post 3", "content": "Content of post 3","id":3},
    {"title":"title of post 4", "content": "Content of post 4","id":4},
    ]

# GET

# @app.get("/")
# async def root():
#     return {"message":"Hello World!!!"}

@app.get("/posts")
def root():
    return my_posts

@app.get('/posts/{id}')
def get_posts(id:int):
    post_id = [p for p in my_posts if p['id'] == id ]
    return {'data': f"{post_id[0]}"}

# POST
@app.post("/posts")
def create_posts(post:Post):
    # print(post.title,"---", post.content, " --- ", post.published, "---", post.rating)
    # print(post.dict())
    post_dict = post.dict()
    post_dict["id"] = randint(0,100000)
    my_posts.append(post_dict)
    return {"data": post_dict}
#title str, content str

# @app.post("/createposts")
# def create_posts():
#     return {"Message": "Successfuly created posts"}

# @app.post("/createpostswithpayload")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title {payload['title']} - content {payload['content']}"}
# #title str, content str

# @app.post("/createpostwithpydantic")
# def create_posts(post:Post):
#     print(post.title,"---", post.content, " --- ", post.published, "---", post.rating)
#     print(post.dict())
#     return {"data": post}




# # Gets

# @app.get('/')
# def index():
#     print('Index function')
#     return 'Hello World!'
#     # return 'olá ' * (1+1)

# @app.get('/blog')
# def new_route():
#     print('new_route function')
#     return {'data':{'name':'Rodrigo'}}

# @app.get('/query-blog')
# def new_route2(limit):
#     return {'data':f'{limit} blogs do DB'}

# # @app.get('/query-params')
# # def new_route2(limit = 10):
# #     return {'data':f'{limit} blogs do DB'}

# @app.get('/query-params')
# def new_route2(limit=10, published:bool=True, sort:Optional[str]=None):
#     if published:
#         return {'data':f'{limit} blogs do DB 2'}
#     else:
#         return {'data':f'{limit} doesn\'t exists'}


# @app.get('/about')
# def about():
#     return 'About page'

# @app.get('/blog/unpublished')
# def unpublished():
#     return {f'data':'all unpublished'}

# @app.get('/blog/{id}')
# def param_route(id):
#     return {'Id':id}

# @app.get('/blog/{id}/comment')
# def comments(id):
#     return {f'comment {id}':f'Comentários do id {id}'}
    
# @app.get('/blog/{id}/content')
# def contents(id: int):
#     return {f'content {id}':id}
    
# @app.get('/blog/{id}/images')
# def images(id: int):
#     return {f'images {id}':id}


# #Creating a class BaseModel to be used on post activity

# class Blog(BaseModel):
#     title:str
#     body:str
#     published: Optional[bool]

# # posts

# @app.post('/blog')
# def create_blog(request: Blog):
#     return {'data': f'Blog criado com {request.title}'}

# # if __name__ == "__main__":
# #     uvicorn.run(app, host="127.0.0.1", port=9000)