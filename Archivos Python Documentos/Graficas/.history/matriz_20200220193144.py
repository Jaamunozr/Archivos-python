import numpy as np
X = np.arange(-2, 12, 1)
print(X)

J=np.sum(X)
J=np.count_nonzero(X)+1
print (J)

n = 1
m = 1
a = [0] * n
for i in range(J):
    a[i] = [0] * m
    print (a)
"""
for i in range(n):
 for j in range(m):
 T[i][j] = M[j][i]"""