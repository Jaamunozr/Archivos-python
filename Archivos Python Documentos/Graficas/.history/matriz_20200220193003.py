import numpy as np
X = np.arange(-2, 12, 1)
print(X)

J=np.sum(X)
J=np.count_nonzero(X)+1
print (J)

n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m
"""
for i in range(n):
 for j in range(m):
 T[i][j] = M[j][i]"""