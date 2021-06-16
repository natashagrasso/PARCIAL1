class Cola (object):

    def __init__(self): #metodo constructor 
        self.__elementos = []

    def arribo (self, dato):  #agregar elementos de la cola
        self.__elementos.append(dato)

    def atencion (self):#sacar elementos de la cola
        return self.__elementos.pop(0)

    def cola_vacia (self):
        return len(self.__elementos)== 0

    def en_frente (self): #devuelve el primer elemento de la cola
        return self.__elementos[0]

    def mover_al_final (self): 
        dato = self.atencion()
        self.arribo(dato) 
        return dato     

    def tamanio(self): #nos devuelve la cantidad de elementos
        return len(self.__elementos) 