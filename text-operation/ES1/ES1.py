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

testo = open("text-operation/ES1/esempio.txt", "r", encoding='UTF8')
libro = testo.read()
testo.close()
print(":::  OTTENUTO IL TESTO       :::")


'''
ESERCIZIO 4
Confrontare Keyword Extraction (selezionare index term)
-   YAKE
-   RAKE
-   spaCy
'''

#                                                               YAKE
import yake
kw_extractor = yake.KeywordExtractor(stopwords=None) # si può personalizzare in molti modi https://github.com/LIAAD/yake
keywords = kw_extractor.extract_keywords(libro)

file_yake = open("text-operation/ES1/yake.txt", "w", encoding='UTF8')

for kw in keywords:
    file_yake.write(repr(kw))
    file_yake.write('\n')
file_yake.close()
print(":::  YAKE FINITO             :::")


#                                                               RAKE
from rake_nltk import Rake

r = Rake()
r.extract_keywords_from_text(libro)
file_rake = open("text-operation/ES1/rake.txt", "w", encoding='UTF8')
rake_list = r.get_ranked_phrases_with_scores()
for w in rake_list:
    file_rake.write(repr(w))
    file_rake.write('\n')
file_rake.close()
print(":::  RAKE FINITO             :::")


#                                                               SPACY    
#                                   NECESSARIO ESEGUIRE python -m spacy download en_core_web_sm
import spacy
import pytextrank

# load a spaCy model, depending on language, scale, etc.
nlp = spacy.load("en_core_web_sm")
# add PyTextRank to the spaCy pipeline
nlp.add_pipe("textrank")

doc = nlp(libro)
# examine the top-ranked phrases in the document
file_spacy = open("text-operation/ES1/spacy.txt", "w", encoding='UTF8')
for phrase in doc._.phrases:
    file_spacy.write(phrase.text)
    file_spacy.write(' ')
    file_spacy.write(repr(phrase.rank))
    file_spacy.write(' ')
    file_spacy.write(repr(phrase.count))
    file_spacy.write('\n')
file_spacy.close()
print(":::  SPACY FINITO            :::")




#tokenizzazione
tokens = nltk.word_tokenize(libro)

file_token = open("text-operation/ES1/1_tokenizzazione.txt", "w", encoding='UTF8')
file_token.write(repr(tokens))
file_token.close()

print(":::  TOKENIZZAZIONE FATTA    :::")


#stopwords eliminatione
from nltk.corpus import stopwords
no_stopwords = [i for i in tokens if i not in stopwords.words("english")]

file_stopwords = open("text-operation/ES1/2_senza_stopwords.txt", "w", encoding='UTF8')
file_stopwords.write(repr(no_stopwords))
file_stopwords.close()

print(":::  STOPWORDS ELIMINATE     :::")


#stemming con lancaster
from nltk.stem.lancaster import LancasterStemmer
lancaster = LancasterStemmer()
stem = [lancaster.stem(t) for t in no_stopwords]

file_stemming = open("text-operation/ES1/3_stemming.txt", "w", encoding='UTF8')
file_stemming.write(repr(stem))
file_stemming.close()

print(":::  STEMMING COMPLETATO     :::")


#selezionare i nomi
# nltk.pos_tag(stem) returna una lista di tuple con (parola,tipo_parola)
nomi = [i[0] for i in nltk.pos_tag(stem) if i[1] == 'NN']

file_nomi = open("text-operation/ES1/4_nomi.txt", "w", encoding='UTF8')
file_nomi.write(repr(nomi))
file_nomi.close()

print(":::  SELEZIONE NOMI FINITA   :::")



