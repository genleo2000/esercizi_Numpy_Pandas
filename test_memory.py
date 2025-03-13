from memory_profiler import profile
import numpy as np

@profile
def min_max():
    ages = np.array([25, 12, 15, 64, 35, 80, 45, 10, 22, 55])
    ages.sort()
    return (ages[0], ages[-1])

if __name__ == "__main__":
    min_max()