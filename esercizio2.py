import math

voti = [92, 85, 88, 95, 87, 93, 98, 86, 90, 94]
mean = sum(voti) / len(voti)

dev = list(map(lambda x: (x - mean)**2, voti))
print(mean)
print(dev)

stddev = math.sqrt(sum(dev) / len(dev))
print(stddev)

import numpy
from numpy.random import default_rng


rng = default_rng(12345)
lista = rng.random(9)
print(lista)
print(lista.reshape(3,3))


# la funzione linspace considera il valore di partenza e quello di arrivo e produce i restanti valori, all'interno dell'intervallo, tutti equidistanti
print(numpy.linspace(0,100,10,endpoint=False).reshape(5,2))
print(numpy.linspace(10,100,10).reshape(5,2))
print(numpy.linspace(0,100,10)) # non produce valori interi
print(numpy.linspace(10,100,10)) # produce valori interi
prd = numpy.linspace(0,100,10)
print(prd[::2])
prd_bd = numpy.linspace(10,100,10).reshape(5,2)
print('\nslicing di array bidimensionale - partenza\n')
print(prd_bd)
print('\nslicing di array bidimensionale\n')
print(prd_bd[::2, -1])
print(prd_bd[1:-2, -1])

print('\nESERCIZIO\n')
ex = numpy.arange(9).reshape(3,3)
print(ex)
print(ex[:2,:]) # si può fare semplicemente ex[:2]
print(ex[:,0])
print(ex[2,1])