import crazy_words
import data_source

text = data_source.get_data__from_keyboard()
crazy_words.principal(text)
crazy_words.dividir_llista_paraules(text)