error = 1E-6 #0.000001

#Entradas 
import sympy as sp
funcion = " (x-3)**3/6-(x-2)**2/4+x-5"
ec = sp.sympify(funcion)   #sympify.-estamos convirtiendo la cadena de expresión en una expresión matemática real 
x = sp.symbols("x")        #podemos declarar algunas variables para el uso de expresiones matemáticas y polinomios
x0 = -0.1
x1 = 0

f2 = 1E10
auxi = 0

while abs(f2) > error:
    auxi = auxi + 1
    print("Iteracion: ", auxi)
    print("x0 = ", x0)
    f0 = ec.subs({x: x0}).evalf()
    print("F(x0) = ", f0)
    print("x1 = ", x1)
    f1 = ec.subs({x: x1}).evalf()
    print("F(x1) = ", f1)
    x2 = x1 - ((ec.subs({x: x1}).evalf() * (x1-x0))/(ec.subs({x: x1}).evalf() - ec.subs({x: x0}).evalf()))
    print("x2 = ", x2)
    f2 = ec.subs({x: x2 }).evalf()
    print("f(x1) = ", f2)
    
    x0 = x1
    x1 = x2
    
print("\n\nIteraciones = ", auxi)
print("x = ", x2 ," \n")