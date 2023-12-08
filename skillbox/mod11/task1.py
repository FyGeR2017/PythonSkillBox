import numpy as np

def mult(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            sum = 0
            for k in range(len(b)):
                sum += a[i][k] * b[k][j]
            row.append(sum)
        result.append(row)
    return result

def np_mult(a, b):
    return np.dot(a, b)

a = np.random.sample((100, 100))
b = np.random.sample((100, 100))

M1 = mult(a, b)
M2 = np_mult(a, b)

print(np.abs(np.array(M1) - M2).sum())