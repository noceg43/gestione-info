'''
Query expansion is the process of supplementing additional terms or phrases to the original query to improve the retrieval performance
- The central problem of query expansion is the selection of the expansion terms based on which user’s original query is expanded
- One possibility is to exploit a thesaurus like Wordnet
- Write a Python algorithm that given a query expressed as a set of words, expands the input query by adding all (or some) word synonyms
'''

from nltk.corpus import wordnet as wn

# returna una lista incasinata non so il metodo per avere solo il termine sinonimo senza Synset('blblb')
def QueryExpantion(query):
    r = []
    for term in str.split(query):
        r.append(wn.synsets(term))
    return r

print(QueryExpantion("cat inside a box"))