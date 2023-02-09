import pandas as pd
import urllib.request
from tqdm import tqdm
from multiprocessing.pool import ThreadPool
import os.path
import json

#
# This gist downloads all series from TMDB. You can easily modify this to download all movies.
# It uses threads to parallelize downloads and speed up this process.
# Depends on python 3. Tested on anaconda.
# Steps:
# 1. download this file from http://files.tmdb.org/p/exports/tv_series_ids_07_05_2020.json.gz and uncompress in the local directory
# 2. create an api key in TMDB site
# 3. set your api key in the script
# 4. install python libs: pandas, tqdm
# 5. run script
#

# TODO: add your api key here
api_key = 'b586e6409d1ab89b937b4708b14edf48'

# Ref: https://developers.themoviedb.org/3/getting-started/daily-file-exports
#jas = json.load(open('movie_ids_11_01_2022giusto.json',"r", encoding= 'cp850'))
#df = pd.DataFrame.from_dict(jas,orient="records")
df = pd.read_json('movie_ids_12_31_2022.json', lines=True, chunksize=1)
#df = pd.read_json('movie_ids_11_01_2022piccolo.json', lines=True)
#print(df)
ids = list()
for chunk in df:
    #print(chunk)
    print(ids)
    ids.append(chunk["id"].tolist())

#id_giusti = [sublist[0] for sublist in ids]
#print(id_giusti)

'''
urls = [(f"./tutti/movies_{id}.json", f"https://api.themoviedb.org/3/movie/{id}?api_key={api_key}") for id in id_giusti]

def log_failed(uri):
    with open('series_failed.txt', 'w') as writer:
        writer.write(uri)

def is_file_exists(path):
    return os.path.isfile(path)

def fetch_url(entry):
    try:
        path, uri = entry
        if not is_file_exists(path):
            urllib.request.urlretrieve(uri, path)

        return path
    except:
        log_failed(uri)

results = ThreadPool(8).imap_unordered(fetch_url, urls)

for path in tqdm(results):
    pass
'''