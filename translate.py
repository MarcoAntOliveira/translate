from googletrans import Translator

def traduzir(texto, destino='en'):
    tradutor = Translator()
    resultado = tradutor.translate(texto, dest=destino)
    return resultado.text

# Exemplo de uso:
texto_original = "Olá, como você está?"
idioma_destino = 'en'  # Código do idioma desejado (por exemplo, 'en' para inglês)

texto_traduzido = traduzir(texto_original, idioma_destino)
print(f'Texto original: {texto_original}')
print(f'Texto traduzido: {texto_traduzido}')