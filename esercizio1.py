import numpy as np

sales = [[i for i in range(6)] for x in range(3)]

sales_array = np.array(sales)
print(sales_array)

print('mdim: ',sales_array.ndim)
print('shape: ',sales_array.shape)
print('size: ',sales_array.size)
print('dtype: ',sales_array.dtype)

print(sales_array + 1)

print(sales_array.T)
print(sales_array.T.shape)
print(sales_array.reshape(2,9)) # il prodotto dei due parametri di input deve essere uguale al valore "size" dell'array

print('\ntest np Ones\n')
print(np.ones((4,2), dtype=int)) # float come type predefinito
print('\ntest np Zeros\n')
print(np.zeros((4,2), dtype=int))
print('\ntest np Arange\n')
print(np.arange(10))
print('\ntest np Linspace\n')
print(np.linspace(0,100,5)); # il valore di stop è inclusivo 
print('\ntest np identity\n')
print(np.identity(15))

from numpy.random import default_rng

rng = default_rng(12345)
test = rng.random(10)
mean, stddev = 5, 1
test_normal = rng.normal(mean, stddev, size=10) # DISTRIBUZIONE NORMALE CON MEDIA E DEVIAZIONE STANDARD
low, high, size = 5, 15, 20
test_integers = rng.integers(low, high, size)
print('\ntest Randomy\n')
print(test)
print(test_normal)
print(test_integers)