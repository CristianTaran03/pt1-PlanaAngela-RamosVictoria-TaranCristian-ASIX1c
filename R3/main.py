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
import logging
from definir_logs import Logger
def main_1():
    try:
        text = data_source.get_data_from_file()
        llista_texto = crazy_words.dividir_llista_paraules(text)
        resultat_final_llista, primera_lletra, ultima_lletra, signes = crazy_words.mix_words(llista_texto)
        resultat_fitxers.resultat_file(resultat_final_llista)
    except:
        print("Error, no s'ha pogut completar l'acció, revisa el fitxer de logs")

def main_2():
    text = recorre_dir.recorrer_arbol_directorios()





if __name__ == '__main__':
    main_1()