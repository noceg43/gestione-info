Possiamo specificare, tramite l'opzione -f (oppure --fonte), la fonte da cui prendiamo i risultati
1 fonte wikipedia
	python .\index.py shark -f wikipedia
2 fonte tmdb
	python .\index.py shark -f tmdb
3 fonti combinate
	python .\index.py shark
_________________________________________________________________________________________________________________

Possiamo specificare il genere dei film restituiti tramite l'opzione -g del comando
4 genere singolo
	python .\index.py shark -g action
5 più generi
	python .\index.py shark -g thriller drama
_________________________________________________________________________________________________________________

Possiamo effettuare prefix e/o postfix query utilizzando il simbolo: *
6 python .\index.py spider*
7 python .\index.py *spider
8 python .\index.py *ing*

Ovviamente più è generica la ricerca più diminuisce il valore del ranking
_________________________________________________________________________________________________________________

9 più parole di ricerca (single word)
Il search engine permette di effettuare ricerche intersezioni di ricerche single word, semplicemente inserendo più parole separate da spazio

python .\index.py soldiers fight
_________________________________________________________________________________________________________________

10 Unione delle funzionalità riportate
Una query che unisce parte delle query riportate nelle altre presentate precedentemente

python .\index.py prince in a castle -f wikipedia -g romance musical