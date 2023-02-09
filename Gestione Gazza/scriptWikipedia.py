'''
import pandas as pd
import json

# Carica il file CSV in un DataFrame
df = pd.read_csv('wiki_movie_plots_deduped.csv')

# Converte il DataFrame in un oggetto JSON
json_file = df.to_json(orient='records')


# Scrive l'oggetto JSON in un file
with open('filmwikipedia.json', 'w') as f:
    f.write(json_file)
'''

import json

# Apre il file di input
with open('filmwikipedia.json', 'r') as file_json:
    # Carica il contenuto del file in un oggetto Python
    dati = json.load(file_json)

# Crea una lista di occorrenze che rispettano il vincolo
occorrenze = [x for x in dati if x['Release Year'] == 2017]
print(len(occorrenze))

# Apre il file di output
#with open('filmwikipedia2017.json', 'w') as file_json_output:
    # Scrive le occorrenze nel file
    #json.dump(occorrenze, file_json_output)



