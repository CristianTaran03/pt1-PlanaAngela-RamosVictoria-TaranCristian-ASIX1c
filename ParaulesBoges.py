"""
Angela Plana, Victoria Ramos, Cristian Taran
22/2/2024
ASIXc M03 UF2 A1
Descripción:Crear un programa  on es demani un nom d'usuari i una contrasenya i la quantitat  d’intents per fer login.
Si l’usuari encerta la combinació de nom d’usuari i contrasenya, el programa li mostrarà el missatge “Benvingut al Sistema!”
i una foto de la seva cara feta amb caràcters ASCII.
"""
import random

lista = []
def mezclar_letras(palabra):
    for x in palabra:
        primera_letra = x[0]
        ultima_letra = x[-1]
        letras_medio = list(x[1:-1])
        random.shuffle(letras_medio)
        palabra_mezclada = primera_letra + ''.join(letras_medio) + ultima_letra
        lista.append(palabra_mezclada)
    return lista
palabra = input("Ingresa una palabra: ")
palabra = palabra.split()
print(palabra)
lista = mezclar_letras(palabra)
print(lista)