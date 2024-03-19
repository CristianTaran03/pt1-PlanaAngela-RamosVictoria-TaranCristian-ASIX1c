import string




def principal(text):
    print(text) 
    llista_dividida = dividir_llista_paraules(text)
    return llista_dividida
    #mix paraules
    #control
    #resultat
    

def dividir_llista_paraules(text):
    llista_text = text.split()
    return llista_text

def mix_words():
    resultat_final_llista = []
    signes = string.punctuation + '¡' + '¿'

    for paraula in :
        primera_lletra = paraula[0]
        ultima_lletra = paraula[-1]