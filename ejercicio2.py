# implementar una función que calcule la suma de todos los números 
# enteros comprendidos entre cero y un número entero positivo dado

def suma(n1):
    if (n1 == 1):
        return n1
    else:
        return n1 + suma (n1-1)   

print(suma(3)) 
