import nltk
# scarica la collection book
#nltk.download()

# scarica scarica
#nltk.download('omw-1.4')


'''
TOKENIZZAZIONE
'''
text = "This is a beautiful text"
tokens = nltk.word_tokenize(text)
print(tokens)


'''
RIMOZIONE DI STOPWORDS e LEMMATIZATION
lemmatization è il contrario dello stemming (camminando --> cammina)
quindi a che serve ? boh
'''
from nltk.corpus import stopwords
wnl = nltk.WordNetLemmatizer()
for t in tokens:
    if not t in stopwords.words("english"):
        print(wnl.lemmatize(t))

'''
STEMMERS
Porter e Lancaster sono 2 famosi
'''
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
print([porter.stem(t) for t in tokens]) #beautiful -> beauti

from nltk.stem.lancaster import LancasterStemmer
lancaster = LancasterStemmer()
print([lancaster.stem(t) for t in tokens]) # beautiful -> beauty


'''
ANALISI GRAMMATICALE

'''
from nltk.corpus import treebank
from nltk.tree import *
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()


