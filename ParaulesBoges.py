"""
Angela Plana, Victoria Ramos, Cristian Taran
27/02/2024
ASIXc M03 UF2 A1
Descripción:Crear un programa  on es demani un nom d'usuari i una contrasenya i la quantitat  d’intents per fer login.
Si l’usuari encerta la combinació de nom d’usuari i contrasenya, el programa li mostrarà el missatge “Benvingut al Sistema!”
i una foto de la seva cara feta amb caràcters ASCII.
"""
import random
import string

#region funcions
def crear_lista(text):
    # Transformem l'input en una llista, separant-lo per paraules.
    llista_text = text.split()
    return llista_text

def mezcla_error(llista):
    # Crear una nova llista on totes les paraules de la llista anterior estan canviades / Control d'errors.
    resultat_llista = []
    for paraula in llista:
        primera_lletra = paraula[0]
        ultima_lletra = paraula[-1]

        if len(paraula) < 3:
            resultat_llista.append(paraula)

        # Deixem els números tal com estan, ignorant els símbols. Així podem llegir preus, hores, fraccions, etc.
        elif paraula.translate(str.maketrans("", "", string.punctuation)).isdigit():
            resultat_llista.append(paraula)

        elif primera_lletra.isalpha() and ultima_lletra.isalpha():
            originals = list(paraula[1: -1])

            #Si qualsevol dels caràcters que hauríem de barrejar és un símbol, deixem la paraula tal com està. Així podem posar enllaços de webs, etc.
            if any(char in string.punctuation for char in originals):
                resultat_llista.append(paraula)
            else:
                random.shuffle(originals)
                canviades = primera_lletra + ''.join(originals) + ultima_lletra
                resultat_llista.append(canviades)

        # La barreja en cas de que el primer i ultim caracter siguin signes de puntuació.
        elif primera_lletra in string.punctuation and ultima_lletra in string.punctuation and len(paraula) >= 5:
            segona_lletra = paraula[1]
            penultima_lletra = paraula[-2]
            originals = list(paraula[2: -2])

            # Tornem a deixar la paraula tal i com està si conté signes entre mig.
            if any(char in string.punctuation for char in originals):
                resultat_llista.append(paraula)
            else:
                random.shuffle(originals)
                canviades = primera_lletra + segona_lletra + ''.join(originals) + penultima_lletra + ultima_lletra
                resultat_llista.append(canviades)

        # La barreja en cas de que el primer caracter sigui un signe de puntuació.
        elif primera_lletra in string.punctuation and len(paraula) >= 4:
            segona_lletra = paraula[1]
            originals = list(paraula[2: -1])

            # Tornem a deixar la paraula tal i com està si conté signes entre mig.
            if any(char in string.punctuation for char in originals):
                resultat_llista.append(paraula)
            else:
                random.shuffle(originals)
                canviades = primera_lletra + segona_lletra + ''.join(originals) + ultima_lletra
                resultat_llista.append(canviades)

        # La barreja en cas de que l'últim caracter sigui un signe de puntuació.
        elif ultima_lletra in string.punctuation and len(paraula) >= 4:
            penultima_lletra = paraula[-2]
            originals = list(paraula[1: -2])

            # Tornem a deixar la paraula tal i com està si conté signes entre mig.
            if any(char in string.punctuation for char in originals):
                resultat_llista.append(paraula)
            else:
                random.shuffle(originals)
                canviades = primera_lletra + ''.join(originals) + penultima_lletra + ultima_lletra
                resultat_llista.append(canviades)

        # Que sempre retorni algo, encara que no canvii la paraula.
        else:
            resultat_llista.append(paraula)

    return resultat_llista
def resultat_string (resultat):
    # Convertir la llista en una cadena nova com a resultat final.
    resultat_final = " ".join(resultat)
    print(resultat_final)
    return resultat_final
#endregion

text = input()
llista = crear_lista(text)
resultat = mezcla_error(llista)
frase_final = resultat_string(resultat)