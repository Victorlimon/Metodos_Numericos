error = 1E-6 #0.0000001

#Entradas 
import sympy as sp
funcion = "2.718281828459045**x + log(x) - 5 "  #"(x-3)**3/6-(x-2)**2/4+x-5"

ec = sp.sympify(funcion)   #sympify.-estamos convirtiendo la cadena de expresión en una expresión matemática real 
x = sp.symbols("x")        #podemos declarar algunas variables para el uso de expresiones matemáticas y polinomios
x0 = 1
x1 = 10
print("Ecuacion = ", ec)
print("x0 = ", x0)
print("x1 = ", x1)

#Proceso
f0 = ec.subs({x: x0}).evalf()
f1 = ec.subs({x0: x1}).evalf()
f2 = 1E10
auxi = 0
while abs(f2) > error:    # abs.-valor absolto
    auxi = auxi + 1
    x2 = ((ec.subs({x: x0}).evalf() * x1)-(ec.subs({x: x1}).evalf() * x0))/(ec.subs({x: x0}).evalf() - ec.subs({x: x1}).evalf())
    print("\n Iteracion: ", auxi)
    print("x0 = ", x0)
    print("f(x0) = ", f0)
    print("x1 = ", x1)
    print("f(x1) = ", f1)
    print("x2 = ", x2)
    f2 = ec.subs({x: x2}).evalf()
    print("f(x2) = ", f2)
    f0 = ec.subs({x: x0}).evalf()
    #f2 = ec.subs({x: x2}).evalf()
    f1 = ec.subs({x: x1}).evalf()
    if ec.subs({x: x0}).evalf() * ec.subs({x: x2}).evalf() < 0:
        x1 = x2
    elif ec.subs({x: x1}).evalf() * ec.subs({x: x2}).evalf() < 0:
        x0 = x2
    else:
        x2 = x2
        
print("\n\n x = ", x2)
print("Iteraciones: ", auxi)
