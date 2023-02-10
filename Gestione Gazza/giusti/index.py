# Importo la libreria argparse per gestire gli argomenti da riga di comando
import argparse
import json
# Importo le librerie necessarie per creare gli indici Whoosh
from whoosh.fields import Schema, TEXT, ID, KEYWORD, STORED
from whoosh.index import *
from whoosh.qparser import *
import time
from whoosh.query import And, Regex, FuzzyTerm


# Inizio a contare il tempo
start = time.perf_counter()

# Inizializzo l'oggetto argparse per gestire gli argomenti da riga di comando
parser = argparse.ArgumentParser()
# Aggiungo l'argomento "fonte", che può avere solo i valori "wikipedia" o "tmdb"
parser.add_argument('-f', '--fonte', choices=['wikipedia', 'tmdb'],
                    help='Seleziona la fonte da cui cercare i risultati')
parser.add_argument("-g", "--genere", nargs='+', help="Specificare i generi da cercare")

# Aggiungo l'argomento "query", che è composto da una lista di parole da cercare
parser.add_argument('query', nargs='+', help='Inserisci le parole da cercare')
# Analizzo gli argomenti passati da riga di comando
args = parser.parse_args()

# Unisco la lista di parole della query in una stringa separata da spazi
query = ' '.join(args.query)
if args.genere is not None:
    generi = ' '.join(args.genere)
else:
    generi = None


# Creo lo schema per gli indici Whoosh, composto da un campo per il titolo (ID) e uno per il contenuto (TEXT)
schema = Schema(title=ID(stored=True), content=TEXT, genres=KEYWORD)

# Creo l'indice per wikipedia
ix_wikipedia = open_dir("index_wikipedia")

# Creo un writer per l'indice
'''
writer_wikipedia = ix_wikipedia.writer()


# Apro il file contenente i dati da wikipedia
with open('wikipediaformattato.json', 'r') as f:
    # Carico il contenuto del file in una lista
    element_list = json.load(f)

# Aggiungo i documenti all'indice
for element in element_list:
    writer_wikipedia.add_document(
        title=element['Title'], content=element['Plot'], genres = element['Genre'])

# Commit delle modifiche all'indice
writer_wikipedia.commit()
'''


# Creo un searcher per l'indice
searcher_wikipedia = ix_wikipedia.searcher()

# Ripeto lo stesso procedimento per l'indice di TMDB
schema = Schema(title=ID(stored=True), content=TEXT, genres=KEYWORD)



ix_TMDB = open_dir("index_TMDB")
'''


writer_TMDB = ix_TMDB.writer()

with open('tmdbformattato.json', 'r') as f:
    # Carico il contenuto del file in una lista
    element_list = json.load(f)

dizionario_id_TMDB = {
    28: "action",
    12: "adventure",
    16: "animation",
    35: "comedy",
    80: "crime",
    99: "documentary",
    18: "drama",
    10751: "family",
    14: "fantasy",
    36: "history",
    27: "horror",
    10402: "musical",
    9648: "mystery",
    10749: "romance",
    878: "sci-fi",
    10770: "TV Movie",
    53: "thriller",
    10752: "war",
    37: "western"
}


for element in element_list:
    writer_TMDB.add_document(
        title=element['title'], content=element['overview'], genres=" ".join([dizionario_id_TMDB[id] for id in element['genre_ids']]))
    




writer_TMDB.commit()
'''
searcher_TMDB = ix_TMDB.searcher()


# Costanti per il calcolo del punteggio combinato
PESO_WIKIPEDIA = 0.3
PESO_TMDB = 0.7


class Film:
    def __init__(self, title, score_wikipedia, score_tmdb):
        """
        Inizializzazione di un'istanza Film
        """
        self.title = title
        self.score_wikipedia = score_wikipedia
        self.score_tmdb = score_tmdb

    def combined_score(self):
        """
        Calcola il punteggio combinato utilizzando i pesi definiti
        """
        return self.score_wikipedia * PESO_WIKIPEDIA + self.score_tmdb * PESO_TMDB

    def __str__(self):
        """
        Restituisce una rappresentazione testuale dell'oggetto Film
        """
        return self.title + f'{self.combined_score():.2f}'


def search(query, source=None, generi=None):
    # Inizializzare una lista vuota per i risultati
    films = []
    results_wikipedia = None
    results_tmdb = None
    # Cercare i risultati su Wikipedia se la fonte è specificata come 'wikipedia'
    if source == 'wikipedia':
        # Creare un parser per la query di ricerca sul contenuto
        content_query = QueryParser("content", ix_wikipedia.schema).parse(query)

        # Se non sono specificati i generi, eseguire una ricerca solo sulla query di contenuto
        if generi is None:
            results_wikipedia = searcher_wikipedia.search(content_query)
        # Altrimenti, eseguire una ricerca combinata sulla query di contenuto e sui generi
        else:
            # Creare una lista di query basate su espressioni regolari per ogni genere
            genres_list = generi.split()
            genres_query = [Regex("genres", ".*" + genre + ".*") for genre in genres_list] 
            # Eseguire la ricerca combinata
            results_wikipedia = searcher_wikipedia.search(And([content_query, *genres_query]))
        print("Risultati da Wikipedia")
        # Per ogni risultato della ricerca,
        for result in results_wikipedia:
            films.append(Film(result['title'], result.score, "wikipedia"))
    # Cercare i risultati su TMDB se la fonte è specificata come 'tmdb'
    elif source == 'tmdb':
        # Creare un parser per la query di ricerca sul contenuto
        content_query = QueryParser("content", ix_TMDB.schema).parse(query)
        # Se non sono specificati i generi, eseguire una ricerca solo sulla query di contenuto
        if generi is None:
            results_tmdb = searcher_TMDB.search(content_query)
            print(results_tmdb)
        # Altrimenti, eseguire una ricerca combinata sulla query di contenuto e sui generi
        else:
            # Creare una lista di query basate su espressioni regolari per ogni genere
            genres_list = generi.split()
            genres_query = [Regex("genres", ".*" + genre + ".*") for genre in genres_list] 
            # Eseguire la ricerca combinata
            results_tmdb = searcher_TMDB.search(And([content_query, *genres_query]))            
        print("Risultati da TMDB")
        # Per ogni risultato della ricerca, creare un oggetto Film e aggiungerlo alla lista dei film
        for result in results_tmdb:
            films.append(Film(result['title'], result.score, "tmdb"))
    # Cercare i risultati sia su Wikipedia che su TMDB se la fonte non è specificata
    elif source is None:
        content_query_wikipedia = QueryParser("content", ix_wikipedia.schema).parse(query)
        content_query_tmdb = QueryParser("content", ix_TMDB.schema).parse(query)

        if generi is None:
            results_wikipedia = searcher_wikipedia.search(content_query_wikipedia)
            results_tmdb = searcher_TMDB.search(content_query_tmdb)
        else:
            genres_list = generi.split()
            genres_query = [Regex("genres", ".*" + genre + ".*") for genre in genres_list]            
            results_wikipedia = searcher_wikipedia.search(And([content_query_wikipedia, *genres_query]))
            results_tmdb = searcher_TMDB.search(And([content_query_tmdb, *genres_query]))            

        print("Risultati combinati:")
        for result in results_wikipedia:
            films.append(Film(result['title'], result.score, "wikipedia"))
        for result in results_tmdb:
            films.append(Film(result['title'], result.score, "tmdb"))
    # Stampare un messaggio di errore se la fonte non è valida e restituire
    else:
        print("Fonte non valida")
        return
    # Creare una lista di istanze Film per tutti i film trovati in entrambe le fonti
    
    films = []
    if results_wikipedia is not None:
        for result in results_wikipedia:
            films.append(Film(result['title'], result.score, 0))

    if results_tmdb is not None:
        for result in results_tmdb:
            films.append(Film(result['title'], 0, result.score))


    # Unire i film con lo stesso titolo
    films_combined = {}
    for film in films:
        if film.title in films_combined:
            current_film = films_combined[film.title]
            films_combined[film.title] = Film(
                film.title,
                current_film.score_wikipedia + film.score_wikipedia,
                current_film.score_tmdb + film.score_tmdb
            )
        else:
            films_combined[film.title] = film

    # Stampare i risultati finali ordinati per punteggio combinato
    for film in sorted(films_combined.values(), key=lambda x: x.combined_score(), reverse=True):
        print(film.title, f'{film.combined_score():.2f}')


search(query, args.fonte, generi)


# query aggiungere tipo "solo film genere" o "solo film rating > x"

# unire fonti dandogli peso
# possibilità usare solo una fonte



# Fine del conteggio del tempo
end = time.perf_counter()

# Stampa il tempo impiegato
print("Tempo impiegato:",f'{( end - start):.2f}', "secondi")





