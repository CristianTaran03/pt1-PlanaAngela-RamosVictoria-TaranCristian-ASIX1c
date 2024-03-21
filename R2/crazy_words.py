"""
Angela Plana, Victoria Ramos, Cristian Taran
19/03/2024
ASIXc M03 UF2 A2

És “qui sap”, és a dir, té implementada la lògica necessària per a convertir un text de paraules “normals”, en un text de “paraules boges”
"""
import string
import data_source
import random

def dividir_llista_paraules(text):
    llista_text = text.split()
    return llista_text

def palabra_simple(paraula, resultat_final_llista,signes, primera_lletra, ultima_lletra):
    originals = list(paraula[1: -1])
    # Si qualsevol dels caràcters que hauríem de barrejar és un símbol, deixem la paraula tal com està. Així podem posar enllaços de webs, etc.
    if any(char in signes for char in originals):
        resultat_final_llista.append(paraula)
    else:
        random.shuffle(originals)
        canviades = primera_lletra + ''.join(originals) + ultima_lletra
        resultat_final_llista.append(canviades)
        return resultat_final_llista

def palabra_2_signes_finals(paraula, resultat_final_llista, signes, primera_lletra, ultima_lletra):
    segona_lletra = paraula[1]
    penultima_lletra = paraula[-2]
    originals = list(paraula[2: -2])

    # Tornem a deixar la paraula tal i com està si conté signes entre mig.
    if any(char in signes for char in originals):
        resultat_final_llista.append(paraula)
    # I si posem 2 signes al final? per exemple una paraula acaba amb ?,
    elif penultima_lletra in signes:
        antep = paraula[-3]
        originals = list(paraula[1: -3])
        random.shuffle(originals)
        canviades = primera_lletra + ''.join(originals) + antep + penultima_lletra + ultima_lletra
        resultat_final_llista.append(canviades)
    else:
        random.shuffle(originals)
        canviades = primera_lletra + segona_lletra + ''.join(originals) + penultima_lletra + ultima_lletra
        resultat_final_llista.append(canviades)
        return resultat_final_llista

def palabra_2_signes_primera_lletra(paraula, resultat_final_llista, signes, primera_lletra, ultima_lletra):
    segona_lletra = paraula[1]
    originals = list(paraula[2: -1])

    # Tornem a deixar la paraula tal i com està si conté signes entre mig.
    if any(char in signes for char in originals):
        resultat_final_llista.append(paraula)
    else:
        random.shuffle(originals)
        canviades = primera_lletra + segona_lletra + ''.join(originals) + ultima_lletra
        resultat_final_llista.append(canviades)
        return resultat_final_llista

def palabra_2_signes_ultima_lletra(paraula, resultat_final_llista, signes, primera_lletra, ultima_lletra):
    penultima_lletra = paraula[-2]
    originals = list(paraula[1: -2])

    # Tornem a deixar la paraula tal i com està si conté signes entre mig.
    if any(char in signes for char in originals):
        resultat_final_llista.append(paraula)

    # I si posem 2 signes al final? per exemple una paraula acaba amb ?,
    elif penultima_lletra in signes:
        antep = paraula[-3]
        originals = list(paraula[1: -3])
        random.shuffle(originals)
        canviades = primera_lletra + ''.join(originals) + antep + penultima_lletra + ultima_lletra
        resultat_final_llista.append(canviades)
    else:
        random.shuffle(originals)
        canviades = primera_lletra + ''.join(originals) + penultima_lletra + ultima_lletra
        resultat_final_llista.append(canviades)
        return resultat_final_llista

def mix_words(llista_text):
    resultat_final_llista = []
    signes = string.punctuation + '¡' + '¿'

    for paraula in llista_text:
        primera_lletra = paraula[0]
        ultima_lletra = paraula[-1]
        if len(paraula) <= 3:
            resultat_final_llista.append(paraula)

        # Deixem els números tal com estan, ignorant els símbols. Així podem llegir preus, hores, fraccions, etc.
        elif paraula.translate(str.maketrans("", "", signes)).isdigit():
            resultat_final_llista.append(paraula)

        elif primera_lletra.isalpha() and ultima_lletra.isalpha():
            palabra_simple(paraula, resultat_final_llista, signes, primera_lletra, ultima_lletra)
        # La barreja en cas de que el primer i ultim caracter siguin signes de puntuació.
        elif primera_lletra in signes and ultima_lletra in signes and len(paraula) >= 5:
            palabra_2_signes_finals(paraula, resultat_final_llista, signes, primera_lletra, ultima_lletra)
        # La barreja en cas de que el primer caracter sigui un signe de puntuació.
        elif primera_lletra in signes and len(paraula) > 4:
            palabra_2_signes_primera_lletra(paraula, resultat_final_llista, signes, primera_lletra, ultima_lletra)
        # La barreja en cas de que l'últim caracter sigui un signe de puntuació.
        elif ultima_lletra in signes and len(paraula) > 4:
            palabra_2_signes_ultima_lletra(paraula, resultat_final_llista, signes, primera_lletra, ultima_lletra)
        # Que sempre retorni algo, encara que no canviï la paraula.
        else:
            resultat_final_llista.append(paraula)

    return resultat_final_llista, primera_lletra, ultima_lletra, signes

def resultat_string (resultat):
    # Convertir la llista en una cadena nova com a resultat final.
    resultat_final = " ".join(resultat)
    print(resultat_final)
    return resultat_final
