# FAST API

## Installing

`pip install fastapi[all]`

> [all] Means that all dependencies will be installed

## Initializing

Importing FastAPI to main.py and instantiating It

    from fastapi import FastAPI

    app = FastAPI()

> Running at CLI : `uvicorn main:app`
>
> If you want to change port number or reload the app automaticly after save some part of project use: `--port "port number" --reload`

## First steps

### GET

First route

    @app.get("/") # this decorator matters a lot. "The path is "/". The HTTP request verb is GET and it is called by app instance decorator
    def root(): # the name of function doesn't matter
        return {"message":"Hello World!!!"} # Once the route has been reached this object is returned to requester as a response in json.

It is possible to use async feature in the function definition, especially qhen making requests that take some time to be fulfilled

    @app.get("/")
    async def root():
        return {"message":"Hello World!!!"}

> the position of routes matters

This method will be called first than get_posts method, because It comes before. Note that both methods have the same route string

    @app.get("/")
    def root():
    return {"message":"Hello World!!!"}

    @app.get('/')
    def get_posts():
    return {'data': "This a post"}

### POST

The requester send to API a request but this time with Data built in. The API server sends back to the requester an answer that providea confirmation of post creation.

Basic post creation without any parameters sended

    @app.post("/createposts")
    def create_posts():
        return {"Message": "Successfuly created posts"}

Post with payload. Data from body

    @app.post("/createpostswithpayload")
    def create_posts(payload: dict = Body(...)):
        print(payload)
        return {"new_post": f"title {payload['title']} - content {payload['content']}"}

## Schemas - Why and how to use

### Why?

- It's pain to get allthe values from the body
- The client can send whatever data they want
- The data isn't geting validated
- We ultimately want to force the client to send data in a schema that we expect

- This is important to validate data and guarantee the correct data management/processing by the server

### How to use?

    class Post(BaseModel):
        title: str
        content: str
        published: bool = True # Default value
        rating: Optional[int] = None  # Optional value of int type (int | None)

    @app.post("/createpostwithpydantic")
    def create_posts(post:Post):
        print(post.title,"---", post.content, " --- ", post.published, "---", post.rating)
        return {"data": "new_post"}

## Docs

## Redocs
