import numpy as np

def np_encode(a):
    unique_elements, counts = np.unique(a, return_counts=True)
    return unique_elements, counts

X = np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])
x, num = np_encode(X)
print("Результат:", x, num)