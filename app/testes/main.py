from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'msg':'Hello World!'}

@app.get('/msg')
async def mensagem():
    return {'msg':'Umas mensagens quaisquer!'}


if __name__ == '__main__':
    import uvicorn

    # uvicorn.run('main:app',host='127.0.0.1',port=3001,log_level='info',reload=True)
    uvicorn.run('main:app',host='0.0.0.0',port=3001,log_level='info',reload=True)