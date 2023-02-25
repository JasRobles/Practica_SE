import nltk
import urllib.request
import re
from inscriptis import get_text
from nltk import word_tokenize, sent_tokenize
from googletrans import Translator
#nltk.download()

#articulo de wikipedia
#enlace = "https://en.wikipedia.org/wiki/Gualaca_bus_crash"
#html = urllib.request.urlopen(enlace).read().decode('utf-8')
Text = "Crockford added a clause to the JSON license stating that The Software shall be used for Good, not Evil, in order to open-source the JSON libraries while mocking corporate lawyers and those who are overly pedantic. On the other hand, this clause led to license compatibility problems of the JSON license with other open-source licenses, as open-source software and free software usually imply no restrictions on the purpose of use"
article_text = Text
article_text = Text.replace("[ edit ]", "")
#print ("###############################")
translator = Translator()

from nltk import word_tokenize, sent_tokenize
#Removing Square Brackets and Extra Spaces
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)

formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

#nltk.download()
#En esta parte hace la tokenizacion
sentence_list = nltk.sent_tokenize(article_text)

#En esta parte encuentra la frecuencia de las palabras
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1

#Calcula las frases que mas se repiten
sentences_socores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 40:
                if sent not in sentences_socores.keys():
                    sentences_socores[sent] = word_frequencies[word]
                else:
                    sentences_socores[sent] += word_frequencies[word]

maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

#Realiza el resumen con las mejores frases
import heapq
summary_sentences = heapq.nlargest(7, sentences_socores, key=sentences_socores.get)
summary = ' '.join(summary_sentences)
traductor = Translator()

Traduccion=traductor.translate(summary, dest='spanish')
print(Traduccion.text)
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()