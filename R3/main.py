"""
Angela Plana, Victoria Ramos, Cristian Taran
19/03/2024
ASIXc M03 UF2 A2

La seva funcionalitat és obtenir les dades, processar-les per a obtenir les “paraules boges” i finalment mostrar-les per pantalla
"""
import crazy_words
import data_source
import definir_logs
import resultat_fitxers
import recorre_dir
import os
import time
from definir_logs import Logger
from definir_logs import Logger2
def main_1():
    try:
        text = data_source.get_data_from_file()
        llista_text = crazy_words.dividir_llista_paraules(text)
        resultat_final_llista, primera_lletra, ultima_lletra, signes = crazy_words.mix_words(llista_text)
        resultat_fitxers.resultat_file(resultat_final_llista)
        Logger.add_to_log('info', 'Completado con exito')
    except:
        Logger.add_to_log('error', 'Error de lectura del fichero paraules.txt')

def main_2():
    tiempo_incio = time.time()
    directorio_entrada, directorio_salida = data_source.create_directory()
    for file in os.listdir(directorio_entrada):
        try:
            archivo = os.path.join(directorio_entrada, file)
            texto = open(archivo, mode='rt', encoding='utf-8')
            text = texto.read()
            llista_texto = crazy_words.dividir_llista_paraules(text)
            resultat_final_llista, primera_lletra, ultima_lletra, signes = crazy_words.mix_words(llista_texto)
            resultat_fitxers.resultat_directory(resultat_final_llista, file, directorio_salida)
            Logger2.add_to_log('info', 'Completada con exito la mezcla de palabras del archivo ' + file)
        except:
            Logger2.add_to_log('error', 'Error en el archivo ' + file)
    tiempo_final = time.time()
    tiempo_ejecucion = round(tiempo_final - tiempo_incio, 2)
    Logger2.add_to_log('info', 'Programa completado en ' + str(tiempo_ejecucion) + ' segundos')


if __name__ == '__main__':
    main_1()
    main_2()