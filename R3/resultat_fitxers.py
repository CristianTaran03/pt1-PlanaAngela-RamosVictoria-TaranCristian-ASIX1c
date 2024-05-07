import logging
from definir_logs import Logger
from definir_logs import Logger2
import os
file = 'boges.log'
def resultat_file(resultat_final_llista):
    try:
        with open('paraules_boges.txt', mode='wt', encoding='utf-8') as text:
            for sublista in resultat_final_llista:
                frase = ' '.join(sublista)
                if sublista == resultat_final_llista[-1]:
                    text.write(frase)
                else:
                    text.write(frase + '\n')
        return text
    except:
        Logger.add_to_log('error', 'Error al escriure el fitxer de paraules boges')
        return False

def resultat_directory(resultat_final_llista, file, directorio_salida):
    try:
        archivo_final = file + "_boges.txt"
        with open(os.path.join(directorio_salida, archivo_final), "w") as text:
            for sublista in resultat_final_llista:
                frase = ' '.join(sublista)
                if sublista == resultat_final_llista[-1]:
                    text.write(frase)
                else:
                    text.write(frase + '\n')
        return text
    except:
        return False