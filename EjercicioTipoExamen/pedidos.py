class Nodo:
    def __init__(self,id_pedido,cliente,estado="Pendiente"):
        self.id_pedido=id_pedido
        self.cliente=cliente
        self.estado=estado
        self.siguiente=None

class ListaEnlazada:
    def __init__(self):
        self.cabeza=None
    
    #Metodos de la clase
    #Agregar un pedido
    def agregar(self,id_pedido,cliente):
        nuevo_Nodo=Nodo(id_pedido,cliente)
        if not self.cabeza:
            self.cabeza=nuevo_Nodo
        else: 
            actual=self.cabeza
            while actual.siguiente:
                actual=actual.siguiente
            actual.siguiente=nuevo_Nodo
    #Metodo para eliminar pedidos
    def eliminar(self,id_pedido):
        if not self.cabeza:
            return None
        if self.cabeza.id_pedido==id_pedido:
            eliminado=self.cabeza
            self.cabeza=self.cabeza.siguiente
            return eliminado
        actual=self.cabeza
        while actual.siguiente and actual.siguiente.id_pedido != id_pedido:
            actual=actual.siguiente
            if actual.siguiente:
                eliminado=actual.siguiente
                actual.siguiente.siguiente
                return eliminado
            return None
    
    #Metodo para mostrar pedidos
    def mostrar(self):
        actual=self.cabeza
        while actual:
            print(f"Pedido Numero: {actual.id_pedido} - Cliente: {actual.cliente} - Estado: {actual.estado} ")
            actual=actual.siguiente

#Cola para procesar los pedidos
class Cola:
    def __init__(self):
        self.items=[]
    
    #Metodos de la cola
    #ENCOLAR
    def encolar(self,pedido):
        self.items.append(pedido)
    
    #DESENCOLAR
    def desencolar(self):
        return self.items.pop(0) if self.items else None
    
    def mostrar(self):
        for pedido in self.items:
            print(f" Pedido Numero: {pedido.id_pedido} - Cliente: {pedido.cliente} - Estado: {pedido.estado}")

class Pila:
    def __init__(self):
        self.items=[]
    
    #Metodos de la pila
    def apilar(self,pedido):
        self.items.append(pedido)
    #Mostrar el historial
    def mostrar(self):
        for pedido in reversed(self.items):
            print(f" Pedido Numero: {pedido.id_pedido} - Cliente: {pedido.cliente} - Estado: {pedido.estado}")


#MENU PRINCIPAL
listaPedidos=ListaEnlazada()
pedidoEnEspera=Cola()
pedidoEnviados=Pila()

id_pedido=1

while True:
    print("1. Agregar nuevo pedido")
    print("2. Procesar el siguiente pedido")
    print("3. Mostrar el Historial de pedidos enviados")
    print("4. Salir")
    opcion=int(input("Seleccione una opcion: "))

    if opcion==1:
        cliente=input("Nombre del cliente: ")
        listaPedidos.agregar(id_pedido,cliente)
        pedidoEnEspera.encolar(Nodo(id_pedido,cliente))
        print(f"Pedido #{id_pedido} agregado correctamente" )
        id_pedido+=1
    elif opcion==2:
        pedido=pedidoEnEspera.desencolar()
        if pedido:
            print(f"Procesando Pedido #{pedido.id_pedido}... ")
            pedido.estado="Procesando"
            listaPedidos.eliminar(pedido.id_pedido)
            pedido.estado="Enviado"
            pedidoEnviados.apilar(pedido)
            print(f" Pedido #{pedido.id_pedido} a sido enviado")
        else:
            print("No hay pedidos pendientes")
    
    elif opcion==3:
        print("HISTORIAL DE PEDIDOS ENVIADOS")
        pedidoEnviados.mostrar()
    elif opcion==4:
        print("Saliendo del sistema de pedidos...")
        break
    else:
        print("Error opcion invalida, intentelo de nuevo!")


