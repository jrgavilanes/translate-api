from googletrans import Translator

translator = Translator()


# print(translator.translate('veritas lux mea', src='la', dest='es').text)

def traducir(texto_a_traducir: str, lenguaje_origen: str = "es", lenguaje_destino: str = "en") -> str:
    """ Traducir un texto dado

        Ej: traducir("hola me llamo Juan", lenguaje_origen="es", lenguaje_destino="en")
    """
    return translator.translate(texto_a_traducir, src=lenguaje_origen, dest=lenguaje_destino).text


def main():
    print(traducir("Hola mi nombre es Juanra"))
    print(traducir("Hola mi nombre es Juanra", lenguaje_destino="it"))
    print(traducir("bla blalalaldkdjflñdafadfaj", lenguaje_destino="it"))


if __name__ == '__main__':
    main()
