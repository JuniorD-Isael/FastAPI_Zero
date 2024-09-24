from http import HTTPStatus

from fastapi import FastAPI

from fast_api_zero.schemas import Message, User

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, Mundo!'}


@app.get('/user', status_code=HTTPStatus.OK, response_model=User)
def user():
    return {'usuario': 'fulano'}
