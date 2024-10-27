#Sistema de gestion de productos 
class Producto:
    def __init__(self,nombre,precio,cantidad):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
        self.siguiente=None #El puntero al siguiente nodo
    
    def mostrarProducto(self):
        print(f"Nombre: {self.nombre} - Precio: {self.precio}Bs - Cantidad: {self.cantidad}")

#Paso 2 crear la lista
class ListaEnlazadaInventario:
    def __init__(self):
        self.cabeza=None
        self.productos=[] #Lista para almacenar productos
    
    #Metodo para agregar un Producto
    def agregarProducto(self,nombre,precio,cantidad):
        nuevo_producto=Producto(nombre,precio,cantidad)
        self.productos.append(nuevo_producto)
        print(f"Producto: {nombre} fue agregado correctamente.")
    
    #Metodo para mostrar los producto en el inventario
    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Productos en el inventario:")
            for producto in self.productos:
                producto.mostrarProducto()
    
    def buscarProducto(self,nombre):
        for producto in self.productos:
            if producto.nombre.lower()==nombre.lower():
                print(f"Producto Disponible: ")
                producto.mostrarProducto()
                return producto
        print(f"Producto {nombre} no esta disponible!")
        return None
    
    def totalValor(self):
        total=0
        for producto in self.productos:
            total+=producto.precio*producto.cantidad
            return total

if __name__=="__main__":
    inventario=ListaEnlazadaInventario()
    #Agregar productos al inventario
    inventario.agregarProducto("Producto1",150,15)
    inventario.agregarProducto("Producto2",200,10)
    inventario.agregarProducto("Producto3",300,20)
    inventario.agregarProducto("Producto4",310,12)
    inventario.agregarProducto("Producto5",450,25)

    #Lista de todos los Productos
    print(f"Lista de productos disponibles")
    inventario.mostrar_productos()

    #Buscar un producto
    print(f"Busqueda de producto")
    busqueda=input("Que producto desea: ")
    inventario.buscarProducto(busqueda)

    #Calculo del total del invetario
    print("Total del Inventario de Productos")
    total=inventario.totalValor()
    print(f"El total del inventario es: {total}Bs")



                    