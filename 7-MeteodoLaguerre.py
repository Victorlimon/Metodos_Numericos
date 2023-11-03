error = 1E-6 #0.000001

#Entradas 
import numpy as np

x0 = 10

# Definir el polinomio
poly = np.array([0.2,-4.2, 35, -147, 324.8, -352.8, 144]) #



f1 = 1E10

while abs(f1) > error:
    n = len(poly) - 1 # grado del polinomio
    f = np.polyval(poly, x0)
    f_derivate = np.polyder(poly)
    f_double_derivate = np.polyder(poly, 2)

    g = np.polyval(f_derivate, x0) / f
    h = g**2 - np.polyval((f_double_derivate) ,x0)/f

    print("grado del polinomio", n)
    print("G: ", g)
    print("H: ", h)

    if g > 0:
        d = n / (g + np.sqrt((n-1)*(n*h - g**2)))
        print("dx = ", d)
    else:
        d = n / (g - np.sqrt((n-1)*(n*h - g**2)))
        print("dx = ", d)

    x1 = x0 - d
    print("X1 = ", x1)

    f1 = np.polyval(poly,x1)
    print("f1 = ", f1)
    x0 = x1










