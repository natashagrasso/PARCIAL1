# Dada una lista con nombres de personajes de la saga de Avengers, resolver las
# siguientes tareas:
# a. Determinar si ‘Thor’ está en la lista, de ser así indicar en qué posición de la
# misma;
# b. Modificar el nombre de ‘Scalet Witch’ a ‘Scarlet Witch’;
# c. Dada una lista auxiliar con los siguientes personajes (‘Black Widow’, ‘Hulk’,
# ‘Rocket Racoonn’, ‘Loki’), agregarlos a la lista principal en el caso de no estar
# cargados. 
# d. Realizar un barrido ascendente y descendente de la lista. 
# e. Mostrar la información del personaje en la posición 5.
# f. Mostrar todos los personajes que comienzan con C o S.
# g. Ahora los datos cambiaron y debe incluir (año de aparición y un campo
# booleano que indica si es héroe True villano False), luego realizar un barrido
# ordenado por nombre y otro por año de aparición. Deberá cargar toda la
# información de nuevo.


from lista import Lista
from random import randint

lista_avengers = Lista()
lista_C = Lista()
lista_S = Lista()

#campo = bool



personajes = [
    {'nombre':'hulk','anio_aparicion':1940},
    {'nombre':'Scalet Witch','anio_aparicion':1963},
    {'nombre':'Dr. Strange','anio_aparicion':1963},
    {'nombre':'Thor','anio_aparicion':2009},
    {'nombre':'Mujer Maravilla','anio_aparicion':1941},
    {'nombre':'capitan america','anio_aparicion':1961},
    
]

lista_aux = [
            {'nombre': 'Black Widow','anio_aparicion':1930 },
            {'nombre': 'Hulk','anio_aparicion':1990 },
            {'nombre': 'Rocket Racoonn','anio_aparicion':2000 },
            {'nombre': 'Loki','anio_aparicion':2007 },
]            


pos_thor = 0
pos = 0

for personaje in personajes:
    lista_avengers.insertar(personaje,'nombre')

for auxiliar in lista_aux:#puntoC
    lista_avengers.insertar(auxiliar,'nombre')    

    

lista_avengers.ordenar('nombre') 
lista_avengers.ordenar('anio_aparicion')     

posnombre = lista_avengers.busqueda('Scalet Witch','nombre') #puntoB
if(posnombre != -1 ): 
    lista_avengers.obtener_elemento(posnombre)['nombre'] = 'Scarlet Witch' 


lista_avengers.barrido()  


for i in range (lista_avengers.tamanio()-1,-1,-1):#lista descendente
    print(lista_avengers.obtener_elemento(i))

for i in range(lista_avengers.tamanio()):
    if (i < lista_avengers.tamanio()):
        personaje = lista_avengers.obtener_elemento(i) 

    if (personaje['nombre'][0] =='C'):#puntoF
        lista_C.insertar(personaje['nombre'])
    if (personaje['nombre'][0] =='S'):
        lista_S.insertar(personaje['nombre'])

    if ('Thor' in personaje['nombre']): #puntoA
        pos_thor = i    


# for i in range(len(lista_aux)):#puntoC
#     if (i < (len(lista_aux))):
#         personaje = lista_aux[i]

#         lista_avengers.insertar(personaje,'nombre')

# lista_avengers.barrido()


print('la info del personaje en la pos 4 es ', lista_avengers.obtener_elemento(4))#puntoE
print('thor se encuentra en la posicion ', pos_thor)    
print('los personajes que comienzan con C, o S  son ') 
lista_C.barrido()
lista_S.barrido()  

       