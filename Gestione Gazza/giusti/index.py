import json
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import *
from whoosh.qparser import *
schema = Schema(title=ID(stored=True), content=TEXT)


ix = create_in("index_wikipedia", schema)

writer = ix.writer()

with open('wikipediaformattato.json', 'r') as f:
    # Carica il contenuto del file in una lista
    element_list = json.load(f)

for element in element_list:
    writer.add_document(title=element['Title'], content=element['Plot'])

writer.commit()

searcher = ix.searcher()

cercato = "spider man"

query = QueryParser("content", ix.schema).parse(cercato)
results = searcher.search(query)
print("                   Cercato           ", cercato)
print("WIKIPEDIA")
for result in results:
    print(result['title'])



schema = Schema(title=ID(stored=True), content=TEXT)


ix = create_in("index_TMDB", schema)

writer = ix.writer()

with open('tmdbformattato.json', 'r') as f:
    # Carica il contenuto del file in una lista
    element_list = json.load(f)

for element in element_list:
    writer.add_document(title=element['title'], content=element['overview'])

writer.commit()

searcher = ix.searcher()

query = QueryParser("content", ix.schema).parse(cercato)
results = searcher.search(query)
print("TMDB")
for result in results:
    print(result['title'])
