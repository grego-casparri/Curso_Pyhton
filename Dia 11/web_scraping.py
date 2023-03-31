import bs4
import requests


resultado = requests.get('https://www.escueladirecta.com/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(sopa.select('title'[0]))

# Definición de una función que toma una función como argumento
def aplicar_funcion(funcion, lista):
    resultado = []
    for elemento in lista:
        resultado.append(funcion(elemento))
    return resultado

# Uso de una función lambda como argumento
numeros = [1, 2, 3, 4, 5]
cuadrados = aplicar_funcion(lambda x: x**2, numeros)

print(cuadrados) # [1, 4, 9, 16, 25]








