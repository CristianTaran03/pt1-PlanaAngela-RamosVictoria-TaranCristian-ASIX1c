"""
Angela Plana, Victoria Ramos, Cristian Taran
19/03/2024
ASIXc M03 UF2 A1

És l’encarregada d’obtenir les dades. En aquesta versió les demanarà per teclat. Tot i que és probable, que en posteriors versions, demani les dades per fitxer.
Per tant, hauré d’implementar el mètode:
"""

text = input()
def get_data__from_keyboard(text):
    """ Aquesta funció recull les dades des del teclat
    Retorna: una única cadena de caràcters"""
    # Transformem l'input en una llista, separant-lo per paraules.
    llista_text = text.split()
    return llista_text

def get_data_from_server(URL):
  """ Aquesta funció recull les dades des d’una API Rest a partir d’una URL
URL example.txt   """

def get_data_from_chatGPT(questio):
 """ Aquesta funció recull la resposta a una pregunta """

#TODO al 3r lliurament
def get_data_from_file(file_name):
   """ Aquesta funció recull les dades des d'un arxiu
 Entrada: Una cadena de caràcters amb el nom del fitxer origen
       Retorna: una única cadena de caràcters"""
