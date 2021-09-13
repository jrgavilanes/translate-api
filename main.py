from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from comunes.pagina_inicio import web_inicio
from comunes.constantes import LANGUAGES

import traductor

app = FastAPI(title="Api traductor", description="Api traducir utilizando api de Google translator", version="0.2")

origins = [
    "*",
    # "http://localhost",
    # "http://localhost:8080",
    # "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')
def startup():
    print("iniciando app")


@app.on_event('shutdown')
def shutdown():
    print("apagando app")


@app.get("/", response_class=HTMLResponse)
async def main():
    return web_inicio


@app.get("/translate/")
async def translate(text: str = "", src: str = "es", dest: str = "en"):
    """Traduce el texto recibido en el idioma original al idioma de destino"""
    if text == "":
        text = traductor.traducir("No has insertado ningún texto a traducir", "es", src)
        raise HTTPException(status_code=201, detail=text)

    try:
        respuesta = {
            'translated_text': traductor.traducir(text, src, dest),
            'src': src,
            'dest': dest
        }

        return respuesta

    except:
        raise HTTPException(status_code=422, detail=text)


class Item(BaseModel):
    text: str = "texto a traducir"
    src: str = 'es'
    dest: str = 'en'


@app.post("/translate/")
async def translate_post(item: Item):
    """Traduce el texto recibido en el idioma original al idioma de destino"""
    i = item.dict()
    text = i['text']
    src = i['src']
    dest = i['dest']

    if text == "":
        text = traductor.traducir("No has insertado ningún texto a traducir", "es", src)
        raise HTTPException(status_code=201, detail=text)

    try:
        respuesta = {
            'translated_text': traductor.traducir(text, src, dest),
            'src': src,
            'dest': dest
        }

        return respuesta

    except:
        raise HTTPException(status_code=422, detail=text)


@app.get("/languages_list")
async def languages_list():
    """Lista de lenguajes disponibles"""
    return LANGUAGES
