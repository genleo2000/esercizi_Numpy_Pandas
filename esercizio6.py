import numpy as np

# Broadcasting

array1 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
array2 = np.array([[2],[2],[2],[2]])

# L'array più piccolo viene esteso per poter essere sommato al primo array
#       [[3 4 5 6]
#       [3 4 5 6]
#       [3 4 5 6]
#       [3 4 5 6]]
print(array1 + array2)

array2 = np.array([[2],[2]]) # E' una forma incompatibile a quella di array1, pertanto l'operazione andrà a generare un'eccezione
#print(array1 + array2)

array2 = np.array([2,3,4,5]) # Per essere compatibile è necessario che una dimensione sia in comune tra i due array
print(array1 + array2)

# Vectorization
# E' la possibilità di eseguire operazioni su array senza il bisogno di ricorrere a cicli, ottenendo chiaramente prestazioni migliori

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Somma vettoriale
result = a + b
print(result)