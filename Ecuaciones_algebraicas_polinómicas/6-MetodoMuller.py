error = 1E-6 #0.000001

#Entradas 
import sympy as sp
import math as mh

funcion = " ((x-3)**3/6)-((x-2)**2/4)+x-5"
ec = sp.sympify(funcion)   #sympify.-estamos convirtiendo la cadena de expresión en una expresión matemática real 
x = sp.symbols("x")        #podemos declarar algunas variables para el uso de expresiones matemáticas y polinomios
x0 = 6.0
x1 = 6.5
x2 = 7.0

f3 = 1E10
auxi = -1


while abs(f3) > error:
    h0 = x1 - x0
    h1 = x2 - x1
    p0 = (ec.subs({x: x1}).evalf() - ec.subs({x: x0}).evalf()) / h0
    p1 = (ec.subs({x: x2}).evalf() - ec.subs({x: x1}).evalf()) / h1
    auxi = auxi+1
    print("Iteraccion: ", auxi)
    a = (p1-p0)/(h0+h1)
    b = p1 + (a*h1)
    c = ec.subs({x: x2}).evalf()
    r = mh.sqrt((b**2)-(4*a*c))

    if b+r > b-r :
        de = b+r
        print("divisor + = ", de)
    else:
        de = b-r
        print("divisor - = ", de)

    print("Rho0 = ", p0)
    print("Rho1 = ", p1)
    print("h0 = ", h0)
    print("h1 = ", h1)
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)

    h = (-2*c)/(de)
    x3 = x2 + h
    print("x3 = ", x3)
    f3 = ec.subs({x: x3}).evalf()
    
    x0 = x1
    x1 = x2
    x2 = x3
    
print("\n\nIteraciones = ", auxi)
print("x = ", x3 ," \n")



