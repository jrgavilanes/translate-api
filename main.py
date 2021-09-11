from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

import traductor

app = FastAPI(title="Api traductor", description="Api traducir utilizando api de Google translator", version="0.1")


@app.on_event('startup')
def startup():
    print("iniciando app")


@app.on_event('shutdown')
def shutdown():
    print("apagando app")


@app.get("/", response_class=HTMLResponse)
async def main():
    return """
        <html>
            <head>
                <title>Some HTML in here</title>
            </head>
            <body>
                <h1>API de janrax's translator</h1>
                <pre>
                - Documentación:  <a href="/docs">/docs</a>
                - Lista de idiomas: <a href="/languages_list">/languages_list</a>
                - Traductor: <a href="/translate/?src=es&dest=en&text=Esto es un texto de prueba">/translate/?src=es&dest=en&text=Esto es un texto de prueba</a>
                </pre>
            </body>
        </html>
        """


@app.get("/translate/")
async def translate(text: str = "", src: str = "es", dest: str = "en"):
    """Traduce el texto recibido en el idioma original al idioma de destino"""
    if text == "":
        text = traductor.traducir("No has insertado ningún texto a traducir", "es", src)
        raise HTTPException(status_code=201, detail=text)

    try:
        respuesta = {
            'respuesta': traductor.traducir(text, src, dest),
            # 'persona': {
            #     'nombre': 'juanra',
            #     'edad': 43,
            # }
        }

        return respuesta

    except:
        raise HTTPException(status_code=422, detail=text)


@app.get("/languages_list")
async def languages_list():
    """Lista de lenguajes disponibles"""
    LANGUAGES = {
        'af': 'afrikaans',
        'sq': 'albanian',
        'am': 'amharic',
        'ar': 'arabic',
        'hy': 'armenian',
        'az': 'azerbaijani',
        'eu': 'basque',
        'be': 'belarusian',
        'bn': 'bengali',
        'bs': 'bosnian',
        'bg': 'bulgarian',
        'ca': 'catalan',
        'ceb': 'cebuano',
        'ny': 'chichewa',
        'zh-cn': 'chinese (simplified)',
        'zh-tw': 'chinese (traditional)',
        'co': 'corsican',
        'hr': 'croatian',
        'cs': 'czech',
        'da': 'danish',
        'nl': 'dutch',
        'en': 'english',
        'eo': 'esperanto',
        'et': 'estonian',
        'tl': 'filipino',
        'fi': 'finnish',
        'fr': 'french',
        'fy': 'frisian',
        'gl': 'galician',
        'ka': 'georgian',
        'de': 'german',
        'el': 'greek',
        'gu': 'gujarati',
        'ht': 'haitian creole',
        'ha': 'hausa',
        'haw': 'hawaiian',
        'iw': 'hebrew',
        'he': 'hebrew',
        'hi': 'hindi',
        'hmn': 'hmong',
        'hu': 'hungarian',
        'is': 'icelandic',
        'ig': 'igbo',
        'id': 'indonesian',
        'ga': 'irish',
        'it': 'italian',
        'ja': 'japanese',
        'jw': 'javanese',
        'kn': 'kannada',
        'kk': 'kazakh',
        'km': 'khmer',
        'ko': 'korean',
        'ku': 'kurdish (kurmanji)',
        'ky': 'kyrgyz',
        'lo': 'lao',
        'la': 'latin',
        'lv': 'latvian',
        'lt': 'lithuanian',
        'lb': 'luxembourgish',
        'mk': 'macedonian',
        'mg': 'malagasy',
        'ms': 'malay',
        'ml': 'malayalam',
        'mt': 'maltese',
        'mi': 'maori',
        'mr': 'marathi',
        'mn': 'mongolian',
        'my': 'myanmar (burmese)',
        'ne': 'nepali',
        'no': 'norwegian',
        'or': 'odia',
        'ps': 'pashto',
        'fa': 'persian',
        'pl': 'polish',
        'pt': 'portuguese',
        'pa': 'punjabi',
        'ro': 'romanian',
        'ru': 'russian',
        'sm': 'samoan',
        'gd': 'scots gaelic',
        'sr': 'serbian',
        'st': 'sesotho',
        'sn': 'shona',
        'sd': 'sindhi',
        'si': 'sinhala',
        'sk': 'slovak',
        'sl': 'slovenian',
        'so': 'somali',
        'es': 'spanish',
        'su': 'sundanese',
        'sw': 'swahili',
        'sv': 'swedish',
        'tg': 'tajik',
        'ta': 'tamil',
        'te': 'telugu',
        'th': 'thai',
        'tr': 'turkish',
        'uk': 'ukrainian',
        'ur': 'urdu',
        'ug': 'uyghur',
        'uz': 'uzbek',
        'vi': 'vietnamese',
        'cy': 'welsh',
        'xh': 'xhosa',
        'yi': 'yiddish',
        'yo': 'yoruba',
        'zu': 'zulu',
    }

    return LANGUAGES
