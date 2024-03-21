"""
Angela Plana, Victoria Ramos, Cristian Taran
19/03/2024
ASIXc M03 UF2 A2

És l’encarregada d’obtenir les dades. En aquesta versió les demanarà per teclat. Tot i que és probable, que en posteriors versions, demani les dades per fitxer.
Per tant, hauré d’implementar el mètode:
"""

def get_data__from_keyboard():
    """ Aquesta funció recull les dades des del teclat
    Retorna: una única cadena de caràcters"""
    text = input()
    return text

def get_data_from_server():
    """ Aquesta funció recull les dades des d’una API Rest a partir d’una URL
    URL example.txt   """
    import requests
    import json
    api_url = 'https://api.api-ninjas.com/v1/chucknorris'
    response = requests.get(api_url, headers={'X-Api-Key': '4i+8EDg6uX7fc7Ws1YtQOA==yVzz3jXQOK7jlbpu'})
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)
        text = data["joke"]
        return text
    else:
        print("Error:", response.status_code, response.text)

def get_data_from_chatGPT():
    """ Aquesta funció recull la resposta a una pregunta """


#TODO al 3r lliurament
def get_data_from_file():
    """ Aquesta funció recull les dades des d'un arxiu
    Entrada: Una cadena de caràcters amb el nom del fitxer origen
    Retorna: una única cadena de caràcters"""
