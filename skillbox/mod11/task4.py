import numpy as np
import scipy.stats as sps
import time

def np_sec_av(X):
    cumsum = np.cumsum(X, axis=1)
    indices = np.arange(1, X.shape[1] + 1)
    result = cumsum / indices.reshape(1, -1)
    return result

A = sps.uniform.rvs(size=10**3)
A = np.reshape(A, (10, 100))
print(A)

start_time = time.time()
S2 = np_sec_av(A)
end_time = time.time()

execution_time = end_time - start_time
print("Результат:", S2)
print("Время выполнения:", execution_time)