#Paso 1 Crear la clase NODO(dato)
class Nodo:
    def __init__(self, dato):
        self.dato=dato #Almacenamietno del valor del nodo
        self.siguiente=None #Direccionamiento que apunta al siguiente nodo en la lista

#Paso 2. Crear la Lista
class ListaEnlazada:
    def __init__(self):
        self.cabeza=None #Inicialmente la lista esta vacia
    
    #Metodos de la clase Lista Enlazada
    def insertarInicio(self,dato):
        nuevoNodo=Nodo(dato) #Crear un nuevo Nodo
        nuevoNodo.siguiente=self.cabeza #EL nuevo nodo apuntara a la actual cabez
        self.cabeza=nuevoNodo #El nuevo nodo se convertira en la nueva cabeza

    def insertarFinal(self,dato):
        nuevoNodo=Nodo(dato) #Creamos un nuevo nodo
        if not self.cabeza:
            self.cabeza=nuevoNodo
            return
        ultimo=self.cabeza
        while ultimo.siguiente: #Recorrido de la lista hasta el ultimo nodo
            ultimo=ultimo.siguiente #APUNTAMOS AL SIGUIENTE NODO
        
        ultimo.siguiente=nuevoNodo
    
    def eliminar(self,dato):
        actual=self.cabeza #Dato actual de la lista
        anterior=None
        while actual and actual.dato!=dato: #Buscamos el nodo a eliminar
            anterior=actual
            actual=actual.siguiente
        if not actual: #SI NO SE ENCUENTRA EL NODO, NO HACER NASDA
            return
        if not anterior: #Si el no a eliminar e la cabeza
            self.cabeza=actual.siguiente
        else:
            anterior.siguiente=actual.siguiente

    def mostrarLista(self):
        actual = self.cabeza
        while actual:  # Recorre la lista imprimiendo los nodos
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")


#Paso 4. Crear los Objetos de la clase
lista=ListaEnlazada()
lista.insertarInicio(10)
lista.insertarInicio(20)
lista.mostrarLista()
lista.insertarFinal(30)

lista.mostrarLista()
lista.eliminar(20)
lista.mostrarLista()
lista.insertarInicio(40)
lista.insertarInicio(50)
lista.insertarInicio(60)
lista.insertarInicio(70)
lista.insertarFinal(80)
lista.insertarFinal(90)
lista.insertarFinal(100)
lista.mostrarLista()





