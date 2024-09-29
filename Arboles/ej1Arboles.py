#Busqueda de datos (Productos, Usuarios, Contactos, Servicios) con arbol binario
#Funcionalidad (AgregarDato)=< Insetrta un nuevo dato en el arbol
#Funcionadlidad (BusquedaDato)
#Funcionalidad (MostrarDatos)

#Paso 1. Definir la clase Nodo
class Nodo:
    def __init__(self,nombre,precio): #Productos
    #def __init__(self,nombre,ci) #
        self.nombre=nombre
        self.precio=precio
        self.izquieda=None
        self.derecha=None

#Paso 2. Crear la clase arbol
class Arbol:
    def __init__(self):
        self.raiz=None
    
    #Paso 3. Crear los metodos de la clase
    #Metodo AgregarProducto
    def insertar(self,nombre,precio):
        if self.raiz is None:
            self.raiz=Nodo(nombre,precio)
            print(f"Producto agregado correactemente a la raiz {nombre} - {precio}")
        else: 
            self.insercionRecursiva(self.raiz,nombre,precio)

    #METODO PARA LA INSERSION RECURSIVA
    def insercionRecursiva(self,nodoActual,nombre,precio):
        if nombre.lower()<nodoActual.nombre.lower():
            if nodoActual.izquierda is None:
                nodoActual.izquierda=Nodo(nombre,precio)
                print(f"Producto {nombre} agregado correctamente a la izquierda {nodoActual.nombre} ")
            else:
                self.insercionRecursiva(nodoActual.izquieda, nombre,precio)
        elif nombre.lower()>nodoActual.nombre.lower():
            if nodoActual.derecha is None:
                nodoActual.derecha=Nodo(nombre,precio)
            else:
                self.insercionRecursiva(nodoActual.derecha,nombre,precio)
        else:
            print(f"El producto {nombre} ya existe...")
            nodoActual.precio=precio

    #Metodo para buscar un producto por su nombre
    def buscarProducto(self,nombre):
        productoEncontrado, precio=self.busquedaRecursiva(self.raiz,nombre)
        if productoEncontrado:
            print(f"Producto encontrado: {nombre} - {precio}Bs")
        else:
            print(f"Producto {nombre} no disponible en la tienda")
        return productoEncontrado

    #Busqueda Recursiva
    def busquedaRecursiva(self,nodoActual,nombre):
        if nodoActual is None:
            return False, None
        if nombre.lower()==nodoActual.nombre.lower():
            return True, nodoActual.precio
        elif nombre.lower()<nodoActual.nombre.lower():
            return self.busquedaRecursiva(nodoActual.izquierda,nombre)
        else:
            return self.busquedaRecursiva(nodoActual.derecha,nombre)


#Funcion principal para el llenado del arbol por parte del usuario
def principal():
    arbol=Arbol()
    while True:
        print("Tienda Online - Estructura de datos")
        print("1. Agregar Productos")
        print("2. Buscar Productos")
        print("3. Mostrar todos los productos")
        print("4. Salir")
        seleccion=input("Seleccione la opcion que desea realizar: ")

        if seleccion== '1':
            nombre=input('Ingrese el nombre del producto: ').strip()
            precio=input('Ingrese el precio del Producto: ').strip()
            if nombre and precio:
                arbol.insertar(nombre,precio)
            else:
                print("El nombre y el precio no pueden estar vacios")
        elif seleccion=='2':
            nombre=input("Ingrese el nombre del producto a buscar: ")
            if nombre:
                arbol.buscarProducto(nombre)
            else:
                print("El nombre no puede estar vacio.")

        elif seleccion=='3':
            return True
        elif seleccion=='4':
            print("Gracias por utilizar la tienda....")
            break
        else: 
            print("Opcion Invalida Selecion una opcion entre 1 y 4")


if __name__=="__main__":
    principal()