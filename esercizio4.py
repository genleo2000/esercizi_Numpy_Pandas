import numpy as np

list = np.array([i for i in range(20) if i % 2 == 0])
print(list)

# si utilizzano & e | al posto di and e or
list_four = list[list % 4 == 0]
print(list_four)

cond = (list > 10) & (list < 15)
list_four = list[cond]
print(list_four)


# in pratica creiamo la condizione "champions > 0" che restituisce un array di valori booleani (in base appunto alla condizione)
# questa condizione possiamo darla in pasto come indice a qualsiasi altro array, purchè sia della stessa dimensione
champions = np.array([5, 2, 0, 1, 5, 0])
player = np.array(['Maldini','Nesta','Nedved','Favalli','Costacurta','Buffon'])
player_with_champions = player[champions > 0]

print(player_with_champions)
print(champions > 0)

where_cond = np.where(champions > 0, 'Ha vinto la Champions','Mai vinta')
print(where_cond)

where_cond = np.where(champions > 0, player,'Mai vinta')
print(where_cond)

where_cond = np.where(champions > 0, 'Campione: '+player,'Mai vinta')
print(where_cond)

# Se alla funzione where si da in pasto solo la condizione, viene restituito l'array degli indici
ages = np.array([25, 12, 15, 64, 35, 80, 45, 10, 22, 55])
indici = np.where(ages >= 18)
print(indici)