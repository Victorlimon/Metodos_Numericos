import numpy as np

print("Descomposicion LU, matrices cuadradas")
m = int (input("Introduce el numero de reglones: "))
matriz = np.zeros([m,m])
u = np.zeros([m,m])
l = np.zeros([m,m])
print("Introducir elementos de la matriz: ")
for r in range(0,m):
    for c in range(0,m):
        matriz[r,c] = (input("Elmento a["+str(r+1)+","+str(c+1)+"]"))
        matriz[r,c] = float(matriz[r,c])
        u[r,c] = matriz[r,c]

for k in range(0,m):
    for r in range(0,m):
        if(k==r):
            l[k,r] = 1
        if(k<r):
            factor = (matriz[r,k]/matriz[k,k])
            l[r,k] = factor
            for c in range(0,m):
                matriz[r,c] = matriz[r,c] - (factor * matriz[k,c])
                u[r,c] = matriz[r,c]

    print("Impresion de resultados: ")
    print("Matriz L: ")
    print(l)
    print("Matriz U: ")
    print(u)