import numpy as np
import time

def np_diag_2k(a):
    diagonal = np.diag(a)
    even_diagonal = diagonal[diagonal % 2 == 0]
    if len(even_diagonal) > 0:
        return np.sum(even_diagonal)
    else:
        return 0

a = np.random.randint(1, 10, size=(5, 5))
print(a)

start_time = time.time()
result = np_diag_2k(a)
end_time = time.time()

execution_time = end_time - start_time
print("Сумма четных диагональных элементов:", result)
print("Время выполнения:", execution_time)