import numpy as np
from numpy.random import default_rng

list = [[i for i in range(7)] for x in range(5)]
list_np = np.array(list)

print(list_np+2)

a = list_np[0, :-2]
b = list_np[:, 3]
print(a)
print(b)
# si possono moltiplicare tra di loro array che hanno la stessa forma
# altrimenti si deve scegliere un valoro numerico singolo
print(a*b)
print(a*2)

print(list_np.sum())

town_a_ages = np.array([25, 45, 70, 34, 58])
town_b_ages = np.array([30, 55, 65, 40, 60])
age_differences = town_a_ages-town_b_ages
print(age_differences)

prices = np.array([10.99, 3.50, 1.40, 8.20])
total_prices = prices+5
print(total_prices.round(1))

rng = default_rng(12345)
discount = rng.random(4)
print((total_prices*(1-discount)).round(2))

list = rng.random(9)
list2 = rng.random(7)
print(list)
print(list[:-2])
print(list[:-2]+list2)
print(list[:-2].reshape(7))