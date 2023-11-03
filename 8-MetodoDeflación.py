error = 1E-6 #0.000001

import numpy as np

x0 = 10

# Definir el polinomio
poly = np.array([0.2,-4.2, 35, -147, 324.8, -352.8, 144])

n = len(poly) - 1 # grado del polinomio

f1 = 1E10

while abs(f1) > error:
    f = np.polyval(poly, x0)
    f_derivate = np.polyder(poly)
    f_double_derivate = np.polyder(poly, 2)

    g = np.polyval(f_derivate, x0) / f
    h = g**2 - np.polyval((f_double_derivate) ,x0)/f



    if g > 0:
        d = n / (g + np.sqrt((n-1)*(n*h - g**2)))

    else:
        d = n / (g - np.sqrt((n-1)*(n*h - g**2)))


    x1 = x0 - d


    f1 = np.polyval(poly,x1)

    x0 = x1
    
print("X: ", x1)



b = np.zeros([n+1])
b = poly
for k in range(n - 2, -1, -1):
    b[k] = poly[k] - b[k+1] * x1

fn = 
print(b)


'''
def Division_Sintetica(a, s):
    n = len(a)
    b = [0] * n
    b[n - 1] = a[n - 1]
    
    for k in range(n - 2, -1, -1):
        b[k] = a[k] - b[k + 
        b[k] = a[k] - b[k + 

        b[k] = a[k] - b

        b[k] = a[k]

        b[k] = a

        b[k]

       
1] * s
    
    
    
   
print('residuo')
    print(b[0])
    
    y = b[
    
    y
1:]
    
   
return y

# Ejecución
resultado = Division_Sintetica([-
resultado = Division_Sintet

resultado = Division
120, -46, 79, -3, -7, 1], -4)
print(resultado)
El código anteriorDivision_Sinteticaes Python y

'''

