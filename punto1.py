# Dada una cola con las notificaciones de las aplicaciones de red social de un Smartphone, de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el
# mensaje, resolver las siguientes actividades:
# c. escribir una función que elimine de la cola todas las notificaciones de
# Facebook;
# d. escribir una función que muestre todas las notificaciones de Twitter, cuyo
# mensaje incluya la palabra ‘Python’, si perder datos en la cola;
# e. utilizar una pila para almacenar temporalmente las notificaciones de
# Instagram y mostrar el contenido de dicha pila. 

from pila import Pila
from cola import Cola

class Notificaciones (object):
    def __init__ (self,app_que_emitio,mensaje, hora): 
        self.app_que_emitio = app_que_emitio
        self.mensaje = mensaje 
        self.hora = hora

cola_notificaciones = Cola()
cola_aux = Cola()
pila_ig = Pila()


notificaciones = Notificaciones('twitter','python', '12:05' )
cola_notificaciones.arribo(notificaciones)
notificaciones = Notificaciones('instagram','a un amigo le gusto tu foto', '7:30 PM')
cola_notificaciones.arribo(notificaciones)
notificaciones = Notificaciones('facebook','hoy es el cumpleaños de un amigo', '15:57')
cola_notificaciones.arribo(notificaciones)
notificaciones = Notificaciones('instagram','a un amigo le ha gustado comentario', '11:40 AM')
cola_notificaciones.arribo(notificaciones)

while(not cola_notificaciones.cola_vacia()):#puntoC
    x = cola_notificaciones.atencion() 
    if (x.app_que_emitio != 'facebook'): 
        cola_aux.arribo(x)
 
while (not cola_aux.cola_vacia()):
    cola_notificaciones.arribo(cola_aux.atencion()) 
 
print('la cola sin los elementos de facebook es ')
cantidad_elementos = 0 
while(cantidad_elementos < cola_notificaciones.tamanio()):
    datos = cola_notificaciones.mover_al_final()
    print(datos.app_que_emitio)    
    cantidad_elementos += 1      


while(not cola_notificaciones.cola_vacia()):#puntoD
    x = cola_notificaciones.atencion()  
    if (x.app_que_emitio =='twitter'):
        mensaje = str(x.mensaje)
        buscado = 'python'
        if (mensaje.find(buscado) == 0):
            print(x.app_que_emitio, mensaje)
    cola_aux.arribo(x)        

    if (x.app_que_emitio == 'instagram'):#PuntoE
        pila_ig.apilar(x) 
   

# while(not pila_ig.pila_vacia()): 
#     x = pila_ig.desapilar()
#     print(x)     

while (not cola_aux.cola_vacia()):
    cola_notificaciones.arribo(cola_aux.atencion())

print('las notificaciones en instagram son ')
print(pila_ig.tamanio())  
