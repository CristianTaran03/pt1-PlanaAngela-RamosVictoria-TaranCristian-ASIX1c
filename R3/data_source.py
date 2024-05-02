"""
Angela Plana, Victoria Ramos, Cristian Taran
30/04/2024
ASIXc M03 UF3 A2

És l’encarregada d’obtenir les dades. En aquesta versió les demanarà per teclat. Tot i que és probable, que en posteriors versions, demani les dades per fitxer.
Per tant, hauré d’implementar el mètode:
"""

def get_data_from_file():
    text = open('paraules.txt', mode='rt', encoding='utf-8')
    text = text.readlines()
    text_str = " ".join(text)
    return text_str

""" Aquesta funció recull les dades des d'un arxiu
Entrada: Una cadena de caràcters amb el nom del fitxer origen
Retorna: una única cadena de caràcters"""
