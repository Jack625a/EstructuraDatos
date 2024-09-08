#Ej1.Crea una clase llamada Pila que simule el comportamiento de una pila (estructura LIFO
#- Last In First Out). La pila debe tener las siguientes funcionalidades:
#1. Método apilar(dato): Añade un nuevo elemento a la pila.
#2. Método desapilar(): Elimina y devuelve el elemento en la parte superior de la
#pila.
#3. Método es_vacia(): Devuelve True si la pila está vacía, de lo contrario,
#devuelve False.
#4. Método mostrar_pila(): Muestra todos los elementos de la pila sin eliminarlos.

class Pila:
    def __init__(self):
        self.datos=[]

    #Metodos de la clase
    def apilar(self,dato):
        self.datos.append(dato)

    def desapilar(self):
        if not self.es_vacia():
            return self.datos.pop()
        else:
            return None
        
    def es_vacia(self):
        return len(self.datos)==0
    
    def mostrar_pila(self):
        print(self.datos)

#Prueba
pila=Pila()
pila.apilar(10)
pila.apilar(20)
pila.apilar(30)
pila.apilar(40)
pila.mostrar_pila()
print ("Elemento desapilado: ",pila.desapilar())
pila.mostrar_pila()