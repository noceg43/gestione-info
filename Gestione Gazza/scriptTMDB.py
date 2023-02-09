import requests
import json

# La tua chiave API
api_key = "b586e6409d1ab89b937b4708b14edf48"

# La prima pagina di risultati
page = 1

# Una variabile che indica se ci sono ancora pagine di risultati da scorrere
more_results = True

# Una lista vuota che conterrà i risultati di tutte le richieste
results = []

while more_results:
  # La richiesta all'API
  url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&primary_release_year=2017&page={page}"
  response = requests.get(url)

  # Verifica che la richiesta sia andata a buon fine
  if response.status_code == 200:
    # Carica i risultati in un dizionario
    data = response.json()

    # Aggiungi i risultati alla lista
    results.extend(data['results'])

    # Scorri l'elenco dei film e stampa l'ID di ciascuno
    #for movie in data['results']:
      #print(movie['id'],movie['release_date'])

    

    # Verifica se ci sono altre pagine di risultati
    if data['page'] < data['total_pages']:
      page += 1
    else:
      more_results = False
  else:
    # Stampa un messaggio di errore
    print("Qualcosa è andato storto!", response.status_code)
    more_results = False

# Apri il file JSON in modalità di scrittura
with open('results.json2017', 'w') as file:
  # Scrivi i risultati in formato JSON nel file
  json.dump(results, file)