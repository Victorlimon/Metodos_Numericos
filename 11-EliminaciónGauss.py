import numpy as np 

m = int(input("Valor de m: "))
n = int(input("Valor de n: "))
matrix = np.zeros((m,n))
vector = np.zeros(n)
x = np.zeros(m)
print("Introdusca la matriz de coeficioente y el vector solucion")
for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)] = (input("Elemento a ["+str(r+1)+" , "+str(c+1)+"]"))
    vector[(r)] = (input("b["+str(r+1)+"]: "))
print(matrix)
for k in range(0,m):
    for c in range(k+1,m):
        factor =  (matrix[r,k]/matrix[k,k])
        vector[r] = vector[r] - (factor*vector[k])
        for c in range(0,n):
            matrix[r,c] = matrix[r,c]-(factor*matrix[k,c])

x[m-1] = vector[m-1]/matrix[m-1,m-1]
print(x[m-1])

for r in range(m-2,-1,-1):
    suma = 0
    for c in range(0,n):
        suma = suma + matrix[r,c] * x[c]
    
    x[r] = (vector[r] - suma)/matrix[r,r]

print("Resutado matriz")
print(matrix)
print("Resultado del vector")
print(vector)
print("Resultados: ")
print(x)

"""
N = length(b);
x = zeros(N,1);
for k =1:1:N-1
for n = k+1:1:N
b(n) = b(n) - A(n,k)*b(k)/A(k,k);
for m=N:-1:k
A(n,m) = A(n,m) - A(n,k)*A(k,m)/A(k,k);
end;
end;
end;
for k=N:-1:1
suma = 0;
for m=k+1:1:N
suma = suma +A(k,m)*x(m);
end;
x(k) = (b(k)-suma)/A(k,k);
end;
"""