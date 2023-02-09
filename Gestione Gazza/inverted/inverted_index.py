import nltk

testo = open("file.txt", "r", encoding='UTF8')
libro = testo.read()

#tokenizzazione
tokens = nltk.word_tokenize(libro)

file_token = open("1_tokenizzazione.txt", "w", encoding='UTF8')
file_token.write(repr(tokens))
file_token.close()

print(":::  TOKENIZZAZIONE FATTA    :::")


#stopwords eliminatione
from nltk.corpus import stopwords
no_stopwords = [i for i in tokens if i not in stopwords.words("english")]

file_stopwords = open("2_senza_stopwords.txt", "w", encoding='UTF8')
file_stopwords.write(repr(no_stopwords))
file_stopwords.close()

print(":::  STOPWORDS ELIMINATE     :::")


#stemming con lancaster
from nltk.stem.lancaster import LancasterStemmer
lancaster = LancasterStemmer()
stem = [lancaster.stem(t) for t in no_stopwords]

file_stemming = open("3_stemming.txt", "w", encoding='UTF8')
file_stemming.write(repr(stem))
file_stemming.close()

print(":::  STEMMING COMPLETATO     :::")


#selezionare i nomi
# nltk.pos_tag(stem) returna una lista di tuple con (parola,tipo_parola)
nomi = [i[0] for i in nltk.pos_tag(stem) if i[1] == 'NN']

file_nomi = open("4_nomi.txt", "w", encoding='UTF8')
file_nomi.write(repr(nomi))
file_nomi.close()

print(":::  SELEZIONE NOMI FINITA   :::")


# this will open the file
file = open('4_nomi.txt', encoding='utf8')
read = file.read()
file.seek(0)
read

# to obtain the
# number of lines
# in file
line = 1
for word in read:
	if word == '\n':
		line += 1
print("Number of lines in file is: ", line)

# create a list to
# store each line as
# an element of list
array = []
for i in range(line):
	array.append(file.readline())

print(array)
