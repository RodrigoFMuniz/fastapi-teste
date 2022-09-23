from fastapi import FastAPI, HTTPException, status

app = FastAPI()


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




@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id:int):# declarandovia type hint o tipo de dados do param
    try:
        curso = cursos[curso_id]
        curso.update({'id':curso_id}) #Insere o valor do ID no final do dicionário, compondo a resposta a requisição
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

if __name__=='__main__':
    import uvicorn

    uvicorn.run("main:app", host='0.0.0.0',port=3001, log_level='info', reload=True, debug=True)