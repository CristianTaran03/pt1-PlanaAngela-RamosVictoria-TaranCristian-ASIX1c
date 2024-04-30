
def resultat_file(resultat):
    text = open('paraules_boges.txt', mode='wt', encoding='utf-8')
    text = text.write(resultat)
    return text