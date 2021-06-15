#insertar el nombre de la diosa griega Atenea en la i-ésima posición debajo de la cima 
# de una pila con nombres de dioses griegos.

from pila import Pila

pila_dioses = Pila ()
pila_aux = Pila()

pila_dioses.apilar('zeus')
pila_dioses.apilar('poseidon')
pila_dioses.apilar('agata')
pila_dioses.apilar('meduza')
pila_dioses.apilar('hermes')
 
posicion_a_insertar = 5

if (pila_dioses.tamanio() >= posicion_a_insertar): #chequeamos que el tamaño sea suficiente
    pos = 0 


    while (not pila_dioses.pila_vacia()and pos < posicion_a_insertar):#controla la cantidad de elementos que tengo que desplazar
        pos +=1
        pila_aux.apilar(pila_dioses.desapilar()) #los paso de una pila a la otra

    pila_dioses.apilar('atenea ')   

    while (not pila_aux.pila_vacia()): #reconstruimos los valores que estan en la pila auxiliar
        pila_dioses.apilar(pila_aux.desapilar())

    while (not pila_dioses.pila_vacia()): #mostramos para chequear que se haya cargado correctamente
        print(pila_dioses.desapilar())
else:
    print('la pila no contiene la cantidad de elementos necesarios')


