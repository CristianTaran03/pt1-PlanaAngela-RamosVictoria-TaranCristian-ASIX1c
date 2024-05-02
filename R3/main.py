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
import logging

logs = definir_logs
text = data_source.get_data_from_file()
llista_texto = crazy_words.dividir_llista_paraules(text)
resultat_final_llista, primera_lletra, ultima_lletra, signes = crazy_words.mix_words(llista_texto)
mix_words = crazy_words.resultat_string(resultat_final_llista)
resultat_final = resultat_fitxers.resultat_file(mix_words)
