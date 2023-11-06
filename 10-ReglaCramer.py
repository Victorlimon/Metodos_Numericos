import numpy as np
def cramer(A,b):
  n = len(b)
  D = np.linalg.det(A)
  x = np.zeros(n)
  for k in range(n):
    AK = A.copy()
    AK[:,k] = b
    DK = np.linalg.det(AK)
    x[k] = DK/D
    print("x",k+1, "=",round(x[k],10))

A = np.array([[1,1,1], [2,3,-2], [3,-2,1]])
b = np.array([4,4,-1])
cramer(A,b)
