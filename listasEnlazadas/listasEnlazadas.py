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
