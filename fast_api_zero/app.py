from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_api_zero.schemas import Message, User

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, Mundo!'}


@app.get('/user', status_code=HTTPStatus.OK, response_model=User)
def user():
    return {'usuario': 'fulano'}


@app.get("/ola-mundo", response_class=HTMLResponse)
def ola_mundo():
    return """
        <html>
          <head>
            <title> Nosso olá mundo!</title>
          </head>
          <body>
            <h1> Olá Mundo </h1>
          </body>
        </html>"""
