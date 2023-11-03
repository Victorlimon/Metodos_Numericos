error = 1E-6 #0.000001

#Entradas 
import sympy as sp
from sympy import diff , symbols
funcion = " (x-3)**3/6-(x-2)**2/4+x-5"
ec = sp.sympify(funcion)   #sympify.-estamos convirtiendo la cadena de expresión en una expresión matemática real 
x = sp.symbols("x")        #podemos declarar algunas variables para el uso de expresiones matemáticas y polinomios
x0 = 0

derivada = sp.diff(funcion,x)
f2 = 1E10
auxi = 0

while abs(f2) > error:
    auxi = auxi + 1
    print("Iteracion: ", auxi)
    print("x0 = ", x0)
    f0 = ec.subs({x: x0}).evalf()
    print("F(x0) = ", f0)
    f1 = derivada.subs({x: x0}).evalf()
    print("F'x0 = ", f1)
    x1 = x0 - (ec.subs({x: x0}).evalf()/derivada.subs({x: x0}).evalf())
    print("x1 = ", x1)
    f2 = ec.subs({x: x1 }).evalf()
    print("f(x1) = ", f2)
    x0 = x1
    
print("\n\nIteraciones = ", auxi)
print("x = ", x1 ," \n")
