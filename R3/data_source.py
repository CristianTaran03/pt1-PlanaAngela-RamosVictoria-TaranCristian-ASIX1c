"""
Angela Plana, Victoria Ramos, Cristian Taran
30/04/2024
ASIXc M03 UF3 A2

És l’encarregada d’obtenir les dades. En aquesta versió les demanarà per teclat. Tot i que és probable, que en posteriors versions, demani les dades per fitxer.
Per tant, hauré d’implementar el mètode:
"""
from definir_logs import Logger

def get_data_from_file():
    try:
        texto = open('paraules.txt', mode='rt', encoding='utf-8')
        text = texto.read()
        return text
    except:
        Logger.add_to_log('error', 'Error al llegir el fitxer')


