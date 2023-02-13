# Importo la libreria argparse per gestire gli argomenti da riga di comando
import argparse
from search_engine import search


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


search(query, args.fonte, generi)