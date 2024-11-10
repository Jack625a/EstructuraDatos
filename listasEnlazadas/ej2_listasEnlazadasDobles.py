#Lista enlazada DOBLE
class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None

#Paso 2. Crear la clase para la lista enlazada Doble
class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza=None
    
    #Paso 3. Crear los metodos de la clase
    #Metodo para insertar el dato al inicio
    def insertarIncio(self,dato):
        nuevoNodo=Nodo(dato)
        if self.cabeza is None:
            self.cabeza=nuevoNodo
        else:
            nuevoNodo.siguiente=self.cabeza
            self.cabeza.anterior=nuevoNodo
            self.cabeza=nuevoNodo
    
    #Metodo para insertar el dato al final
    def insertarFinal(self,dato):
        nuevoNodo=Nodo(dato)
        if self.cabeza is None:
            self.cabeza=nuevoNodo
        else:
            temporal=self.cabeza
            while temporal.siguiente:
                temporal=temporal.siguiente
                temporal.siguiente=nuevoNodo
                nuevoNodo.anterior=temporal

    #Metodo para mostrar los datos desde el inicio
    def mostrarListaInicio(self):
        datos = []
        temporal = self.cabeza
        while temporal:
            datos.append(temporal.dato)
            temporal = temporal.siguiente
        print("Lista desde el inicio:", datos)
    #Metodo para mostrar los datos desde el final
    def mostrarListaFinal(self):
        datos=[]
        temporal=self.cabeza
        while temporal and temporal.siguiente:
            temporal=temporal.siguiente
            while temporal:
                datos.append(temporal.dato)
            print("Lista de datos desde el final ", datos)


#Ejemplo de uso 
listaDoble=ListaEnlazadaDoble()
listaDoble.insertarIncio(3)
listaDoble.insertarIncio(4)
listaDoble.insertarIncio(2)
listaDoble.insertarFinal(5)
#Mostrar los datos desde el iniicio
listaDoble.mostrarListaInicio()

#listaDoble.insertarFinal(8)
#listaDoble.mostrarListaInicio()
#Mostrar los datos desde el final
#listaDoble.mostrarListaFinal()