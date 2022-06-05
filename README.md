# FAST API

## Installing

> pip install fastapi[all]

> [all] Means that all dependencies will be installed

## Initializing

> Importing FastAPI to main.py and instantiating It

    from fastapi import FastAPI

    app = FastAPI()

> Running at CLI : `uvicorn main:app`

> If you want to change port number or reload the app automaticly after save some part of project use: `--port "port number" --reload`

## First steps

> First route

    @app.get("/") # this decorator matters a lot. "The path is "/". The HTTP request verb is GET and it is called by app instance decorator
    def root(): # the name of function doesn't matter
        return {"message":"Hello World!!!"} # Once the route has been reached this object is returned to requester as a response in json.

> It is possible to use async feature in the function definition, especially qhen making requests that take some time to be fulfilled

    @app.get("/")
    async def root():
        return {"message":"Hello World!!!"}

## Docs

## Redocs
