
from search_engine import search



# QUERY FONTI
search(query="shark", source="wikipedia")
print('\n')
search(query="shark", source="tmdb")
print('\n')
search(query="shark")
print('\n')


# QUERY GENERE
search(query="shark", generi= "action")
print('\n')
search(query="shark", generi= "thriller drama")
print('\n')


# QUERY POST/PREFIX
search(query="spider*")
print('\n')
search(query="*spider")
print('\n')
search(query="*ing*")
print('\n')


# QUERY PAROLE MULTIPLE
search(query="soldiers fight")
print('\n')


# QUERY TUTTO
search(query="prince in a castle", source="wikipedia", generi="romance musical")
print('\n')
