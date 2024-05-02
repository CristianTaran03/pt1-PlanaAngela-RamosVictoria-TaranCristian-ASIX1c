import logging
from definir_logs import Logger
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
        Logger.add_to_log('info', 'Completado con exito')
        return text
    except:
        Logger.add_to_log('error', 'Error al escriure el fitxer de paraules boges')
        return False