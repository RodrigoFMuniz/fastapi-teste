# FAST API

# API concepts

## O que é?

> É uma interface de comunicação de aplicações de forma programática

## Stateless

> - Toda requisição HTTP é stateless
> - Desta maneira é necessária a validação dos dados pelo cliente.
> - A cada requisição é como se fosse uam nova apresetação entre as partes.

## Endpoints

> - Recursos
> - Categorias ou individuos
> - CRUD
> - Verbos HTTP (GET, POST, PUT, DELETE, PATCH ) e substantivos - recursos(Categorias, produtos, models)
> - URI's

### HTTP GET
<<<<<<< HEAD
> - Indivíduo
> - Coleção

### HTTP POST
> - Coleção - Utilizado para adicionar um individuo à coleção
=======

> - Indivíduos
> - Coleções

### HTTP POST

> - Cria um indivíduo em uma coleção.
> - Acessa coleções.

### HTTP PUT

> - Atualiza indivíduos.
> - Deve ser aplicado somente em indivíduos.

### HTTP DELETE

> - Deleta indivíduos.
> - Deve ser aplicado somente em indivíduos.

## Requests

### Query Strings

> - Vem após a interrogação(question mark)
> - É um conjunto chave:valor
> - É usado para enviar à API, uma requisição especifica
> - Ex.: `..v1/produtos?format=xml`

### Requests via URI

> - Podemos solicitar diretamente passando a extensão
> - `.../v1/produtos.xml`

### Cabeçalho da Request

> - Especifica o formato do arquivo que o requisitante deseja
> - Accept: aplicativo/xml

### Language

> - Especifica o idioma do conteúdo
> - Accept-Language

### Cache Control

> - Especifica se o conteúdo pode ser consumido só o cache e em quanto tempo este é utilizado.

### Versão da API

> - É possível criar versões distintas da API

## Responses

### Cabeçalho da response

> - Possui vários metadados sobre a resposta, como: Content-Type, Las-Modified, Expires, Status.. etc.

### Códigos de status

> - 1xx - Informational
> - 2xx - Success
> - 3xx - Redirection
> - 4xx - Client Error
> - 5xx - Server Error

### Formato de dados

> - XML
> - JSON - mais usado - javascript object notation

## Segurança

### Autenticação

> - Quem é você.
> - Necessário para gerar o token de autenticação
> - Define os níveis de autorização

### Autorização

> - O que você é.
> - CRUD.
> - Autoriza acessos distintos, pós autenticação.

### Tokens

> - Chave criptografada que identifica o cliente.
> - Quando o cliente cria uma conta na sua aplicação, ele recebe uma chave (Public Key).
> - Através desta chave(token), este envia no cabeçalho, ou no corpo da requisição para realizar a autenticação.
> - Como as requisições HTTP são stateless, este token de autenticação sempre é enviado.
>>>>>>> 7184d61ec2859a7715b37c99550008f45e8dd5a7

## Installing

`pip install fastapi[all]`

> [all] Means that all dependencies will be installed

## Initializing

Importing FastAPI to main.py and instantiating It

    from fastapi import FastAPI

    app = FastAPI()

> Running at CLI : `uvicorn app.main:app --port 3000 --reload`
>
> If you want to change port number or reload the app automaticly after save some part of project use: `--port "port number" --reload`

## CRUD

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

### Get with id

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


    @app.post("/posts", status_code=status.HTTP_201_CREATED)
    def create_posts(post:Post):
        # print(post.title,"---", post.content, " --- ", post.published, "---", post.rating)
        # print(post.dict())
        post_dict = post.dict()
        post_dict["id"] = randint(0,100000)
        my_posts.append(post_dict)
        return {"data": post_dict}

### UPDATE

    @app.put("/posts/{id}")
    def update_post(id:int, post:Post):
        index = find_index_post(id)
        if index == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} doesn't exist")
        post_dict = post.dict()
        post_dict['id'] = id
        my_posts[index] = post_dict
        return {'data': post_dict}

### DELETE

    @app.delete("/posts/{id}")
    def delete_post(id:int):
        index = find_index_post(id)
        print(index)
        print(id)
        my_posts.pop(index)
        return {'message': f'post {id} succesfully deleted'}

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

`http://127.0.0.1:3000/docs`

## Redoc

`http://127.0.0.1:3000/redoc`

## status code

`https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml`

## Alchemy

### Database concepts

- Is a collection of organized data that can be easily accessed and managed
- Instead make use of a software referred to as a database management system(DBMS)
- Relational databases:
  - MySQL
  - POSTGRESQL
  - ORACLE
  - SQL Server
- NoSQL databases:
  - MongoDB
  - DynamoDB
  - Oracle
  - SQL Server
- Structured Query Language
  - Language used to communicate with DBMS
