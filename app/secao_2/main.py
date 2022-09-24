from fastapi import FastAPI, HTTPException, status, Response, Path, Query, Header, Depends

from typing import Any, Optional

from models import Curso

from time import sleep

app = FastAPI()

def db_fake():
    try:
        print('Abrindo conexão com db')
        sleep(3)
    finally:
        print('Finalizando ...')
        sleep(2)
        print('Fechando conexão com db')



cursos = {
    1:{
        'titulo':'Curso 1 Codevibes',
        'aulas':40,
        'horas':20
    },
    2:{
        'titulo':'Curso 2 Codevibes',
        'aulas':59,
        'horas':34
    },
    3:{
        'titulo':'Curso 3 Codevibes',
        'aulas':26,
        'horas':29
    },
    4:{
        'titulo':'Curso 4 Codevibes',
        'aulas':12,
        'horas':2
    },
    5:{
        'titulo':'Curso 5 Codevibes',
        'aulas':126,
        'horas':10
    },
    6:{
        'titulo':'Curso 6 Codevibes',
        'aulas':202,
        'horas':18
    },
}



#GET

@app.get('/cursos')
async def get_cursos(db: Any =  Depends(db_fake)):
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id:int = Path(default=None, title="Titulo", description="Descrição do item", gt=0, lt=10), db: Any =  Depends(db_fake)):# declarando via type hint o tipo de dados do param
    try:
        curso = cursos[curso_id]
        if curso_id>6:
            curso.id = curso_id
        else:
            curso.update({'id':curso_id}) #Insere o valor do ID no final do dicionário, compondo a resposta a requisição
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

 # POST

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso:Curso, db: Any =  Depends(db_fake)):
    next_curso:int = len(cursos) + 1
    cursos[next_curso] = curso
    del curso.id
    return curso
    # if next_curso not in cursos:
    #     del curso.id
    #     cursos.update({next_curso: curso})        
    #     return curso
    # else:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Já existe um curso com id {curso.id}")


@app.put('/cursos/{curso_id}')
async def put_cursos(curso_id: int, curso: Curso, db: Any =  Depends(db_fake)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe item com o ID {curso_id}")


@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int, db: Any =  Depends(db_fake)):
    if curso_id in cursos:
        cursos.pop(curso_id)
        # return {"detail": f"Curso {curso_id} deletado com sucesso"} # funciona, porém o status code fica errado
        # return JSONResponse(content="Item deletado",status_code=status.HTTP_204_NO_CONTENT) # Não funciona adequadamente
        return Response(status_code=status.HTTP_204_NO_CONTENT)# funciona
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"O item ID {curso_id} não está no banco de dados.")


# Query paramenter

@app.get('/calculadora')
async def calcular(a:int = Query(default=None, gt=10),b:int = Query(default=None, gt=5),c:Optional[int]=0, geek: str= Header(default=None), db: Any =  Depends(db_fake)):
    res = a+b+c
    print(f'X-GEEK: {geek}')
    return {"Resultado": res}


if __name__=='__main__':
    import uvicorn

    uvicorn.run("main:app", host='0.0.0.0',port=3001, log_level='info', reload=True, debug=True)