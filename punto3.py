# Dado un vector con personaje de las películas de la saga de Star Wars resolver las
# siguientes actividades:
# a. Realizar un barrido recursivo del vector. 
# b. Realizar una función recursiva que permita determinar si ‘Yoda’ está en el
# vector y en que posición.



personajes = ['hulk' , 'capitan america', 'yoda', 'leia' , 'batman']

def star_wars (personajes, pos):
    if(pos < len(personajes) -1):
        if (personajes [pos] == 'yoda'):   #puntoB
            print ('yoda se encuentra en la posicion: ', pos)
            return pos
        else:
            return star_wars(personajes, pos+1)
    else:
        return -1 

print(star_wars(personajes, 0 ))