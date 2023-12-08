import numpy as np

def np_transformation(X, a=1):
    new_array = np.copy(X)
    new_array[1::2] = a
    new_array[::2] = np.power(new_array[::2], 3)
    reversed_array = np.flip(new_array)
    result = np.concatenate((X, reversed_array))
    return result

X = np.array([i for i in range(1, 10, 2)])
S2 = np_transformation(X, 5)
print("Результат:", S2)