#pip install googletrans==3.1.0a0

from googletrans import Translator

translator = Translator()

text = "Halo Dunia"
translation = translator.translate(text, src="id", dest="en")

#print(text.translation)