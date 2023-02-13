
from search_engine import search



# QUERY FONTI
'''
search(query="shark", source="wikipedia")
print('\n')
search(query="shark", source="tmdb")
print('\n')
search(query="shark")
print('\n')

shark
Risultati da Wikipedia
47 Meters Down 11.84
The Lego Ninjago Movie 5.58
The Lego Batman Movie 2.97
The Fate of the Furious 2.92
Tempo impiegato: 0.03 secondi


shark
Risultati da TMDB
Phelps vs Shark 6.70
Trailer Park Shark 6.57
House Shark 6.46
Joe Mande's Award-Winning Comedy Special 5.75
The King of Minami Returns: The Price of a Life 5.75
The King of Minami The Movie 5.75
Kim Swims 5.33
Toxic Shark 5.25
47 Meters Down 5.11
Cebiche de Tiburón 4.97
Tempo impiegato: 0.03 secondi


shark
Risultati combinati:
47 Meters Down 16.95
Phelps vs Shark 6.70
Trailer Park Shark 6.57
House Shark 6.46
Joe Mande's Award-Winning Comedy Special 5.75
The King of Minami Returns: The Price of a Life 5.75
The King of Minami The Movie 5.75
The Lego Ninjago Movie 5.58
Kim Swims 5.33
Toxic Shark 5.25
Cebiche de Tiburón 4.97
The Lego Batman Movie 2.97
The Fate of the Furious 2.92
Tempo impiegato: 0.03 secondi
'''

# QUERY GENERE
'''
search(query="shark", generi= "action")
print('\n')
search(query="shark", generi= "thriller drama")
print('\n')

shark
Risultati combinati:
The Lego Ninjago Movie 6.18
The Yass Film: Adventure to Gaylord Street 5.67
Empire of the Sharks 5.54
Cross Wars 4.52
The Lego Batman Movie 3.57
The Fate of the Furious 3.52
Stray Dogz 5 3.38
Tempo impiegato: 0.05 secondi


shark
Risultati combinati:
47 Meters Down 6.51
Cage Dive 5.53
Tempo impiegato: 0.04 secondi
'''


# QUERY POST/PREFIX
'''
search(query="spider*")
print('\n')
search(query="*spider")
print('\n')
search(query="*ing*")
print('\n')


spider*
Risultati combinati:
Spider-Man: Homecoming 11.28
Spider Jazz 8.15
A Fan's Guide to Spider-Man: Homecoming 7.55
Red 7.55
Gummy-Man 6.82
Anjelah Johnson: Mahalo & Goodnight 6.53
Beside Bowie: The Mick Ronson Story 6.08
Journey to the West: The Legend of the Mermaid 5.63
Journey to the West: The Demons Strike Back 5.37
The White World According to Daliborek 4.55
Amazing Mighty Micro Monsters 3D 4.08
The Mummy 3.94
Ghost in the Shell 3.12
Tempo impiegato: 0.04 secondi


*spider
Risultati combinati:
Spider-Man: Homecoming 11.28
Spider Jazz 8.15
A Fan's Guide to Spider-Man: Homecoming 7.55
Red 7.55
Gummy-Man 6.82
Journey to the West: The Legend of the Mermaid 5.63
Journey to the West: The Demons Strike Back 5.37
The Spider's Web: Britain's Second Empire 4.06
The Mummy 3.94
Ghost in the Shell 3.12
Tempo impiegato: 0.21 secondi


*ing*
Risultati combinati:
Along with the Gods: The Two Worlds 0.70
Puss in Book: Trapped in an Epic Tale 0.70
Coco 0.70
John Wick: Chapter 2 0.70
Spider-Man: Homecoming 0.70
Transformers: The Last Knight 0.70
Cars 3 0.70
The Foreigner 0.70
Justice League 0.70
Power Rangers 0.70
Underworld: Blood Wars 0.30
Monster Trucks 0.30
The Bye Bye Man 0.30
Sleepless 0.30
The Book of Love 0.30
Split 0.30
xXx: Return of Xander Cage 0.30
The Resurrection of Gavin Stone 0.30
Trespass Against Us 0.30
Sophie and the Rising Sun 0.30
Tempo impiegato: 0.92 secondi
'''

# QUERY PAROLE MULTIPLE
'''
search(query="soldiers fight")
print('\n')


soldiers fight
Risultati combinati:
Pride of the Buffalo Soldier 9.81
Darkest Hour 9.46
Bölük 7.35
Furious 6.26
The Frozen Front 6.12
Dead Trigger 6.01
The Beguiled 4.73
Brotherhood of Blades 2 4.69
Tempo impiegato: 0.04 secondi
'''

# QUERY TUTTO
'''
search(query="prince in a castle", source="wikipedia", generi="romance musical")
print('\n')


prince in a castle
Risultati da Wikipedia
Beauty and the Beast 12.41
Tempo impiegato: 0.04 secondi
'''