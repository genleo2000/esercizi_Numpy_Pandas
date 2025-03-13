import numpy as np
from numpy.random import default_rng

rng = default_rng()
value = rng.integers(0,100,20).reshape(2,10)
print(value)

# FUNZIONI AGGREGATRICI
print(value.sum())
print(value.sum(axis=0))
print(value.sum(axis=1))
print(value.mean())
print(value.std()) # deviazione standard

print(np.median(value)) # a differenza della funzione mean (che è un metodo della classe ndarray), è una funzione globale
print(np.sort(value))
print(value[-1, -1]) # la funzione sort, essendo appunto globale, non modifica direttamente l'oggetto

ages = np.array([25, 12, 15, 64, 35, 80, 45, 10, 22, 55])
ages_sorted = np.sort(ages)
print(ages_sorted)
ages.sort() # questa modifica direttamente l'oggetto essendo un metodo della classe ndarray
print(ages) 