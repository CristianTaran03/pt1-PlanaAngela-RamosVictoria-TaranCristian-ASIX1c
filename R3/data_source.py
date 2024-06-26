"""
Angela Plana, Victoria Ramos, Cristian Taran
30/04/2024
ASIXc M03 UF3 A2

És l’encarregada d’obtenir les dades. En aquesta versió les demanarà per teclat. Tot i que és probable, que en posteriors versions, demani les dades per fitxer.
Per tant, hauré d’implementar el mètode:
"""
from definir_logs import Logger
import os

def get_data_from_file():
    try:
        texto = open('paraules.txt', mode='rt', encoding='utf-8')
        text = texto.read()
        return text
    except:
        Logger.add_to_log('error', 'Error de lectura del fichero paraules.txt')

def create_directory():
    directorio_entrada = "./entrada"
    directorio_salida = "./sortida"
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)
    if not os.path.exists(directorio_entrada):
        os.makedirs(directorio_entrada)
    return directorio_entrada, directorio_salida
