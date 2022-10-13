'''
ESERCIZIO 1
- Prendere Dracula
- Tokenization
- Elimination of stopwords
- Stemming
- Selection of nouns
Given a text item, your program will therefore output the 
keywords that could be used to index it. 
'''

import nltk

testo = open("ES1/dracula.txt", "r", encoding='UTF8')
libro = testo.read()
testo.close()
print(":::  OTTENUTO IL TESTO       :::")


#tokenizzazione
tokens = nltk.word_tokenize(libro)

file_token = open("ES1/1_tokenizzazione.txt", "w", encoding='UTF8')
file_token.write(repr(tokens))
file_token.close()

print(":::  TOKENIZZAZIONE FATTA    :::")


#stopwords eliminatione
from nltk.corpus import stopwords
no_stopwords = [i for i in tokens if i not in stopwords.words("english")]

file_stopwords = open("ES1/2_senza_stopwords.txt", "w", encoding='UTF8')
file_stopwords.write(repr(no_stopwords))
file_stopwords.close()

print(":::  STOPWORDS ELIMINATE     :::")


#stemming con lancaster
from nltk.stem.lancaster import LancasterStemmer
lancaster = LancasterStemmer()
stem = [lancaster.stem(t) for t in no_stopwords]

file_stemming = open("ES1/3_stemming.txt", "w", encoding='UTF8')
file_stemming.write(repr(stem))
file_stemming.close()

print(":::  STEMMING COMPLETATO     :::")


#selezionare i nomi
# nltk.pos_tag(stem) returna una lista di tuple con (parola,tipo_parola)
nomi = [i[0] for i in nltk.pos_tag(stem) if i[1] == 'NN']

file_nomi = open("ES1/4_nomi.txt", "w", encoding='UTF8')
file_nomi.write(repr(nomi))
file_nomi.close()

print(":::  SELEZIONE NOMI FINITA   :::")