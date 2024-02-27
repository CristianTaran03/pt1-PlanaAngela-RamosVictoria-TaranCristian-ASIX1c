"""
Angela Plana, Victoria Ramos, Cristian Taran
22/2/2024
ASIXc M03 UF2 A1
Descripción: Implementar en Python un programa que demani una frase per teclat i la retorni per pantalla amb les
lletres de cada paraula de la frase desordenada, tal com diu l’estudi de la Universitat de Cambridge.
"""
import random
import string

def crear_lista(text):
    # Transformem l'imput en una llista, separant-lo per paraules.
    llista_text = text.split()
    return llista_text

def mezcla_error(llista):
    # Crear una nova llista on totes les paraules de la llista anterior estan canviades / Control d'errors.
    resultat_llista = []
    for x in llista:
        primera_lletra = x[0]
        ultima_lletra = x[-1]

        if len(x) <= 2:
            resultat_llista.append(x)
        #si la palabra es un numero o un numero con decimales deja la palabra igual
        elif x.isdigit():
            resultat_llista.append(x)
        #si la palabra es un numero con decimales deja la palabra igual
        elif x.replace('.', '', 1).isdigit() or x.replace(',', '', 1).isdigit():
            resultat_llista.append(x)
        elif primera_lletra not in string.punctuation and ultima_lletra not in string.punctuation:
            originals = list(x[1: -1])
            random.shuffle(originals)
            canviades = primera_lletra + ''.join(originals) + ultima_lletra
            resultat_llista.append(canviades)
        else:
            segona_lletra = x[1]
            penultima_lletra = x[-2]
            originals = list(x[2: -2])
            if len(x) > 5:
                random.shuffle(originals)
                canviades = primera_lletra + segona_lletra + ''.join(originals) + penultima_lletra + ultima_lletra
                resultat_llista.append(canviades)
            else:
                resultat_llista.append(x)

    return resultat_llista
def resultat_string (resultat):
    # Convertir la llista en una cadena nova com a resultat final.
    resultat_final = " ".join(resultat)
    print(resultat_final)
    return resultat_final


text = input()
llista = crear_lista(text)
resultat = mezcla_error(llista)
frase_final = resultat_string(resultat)