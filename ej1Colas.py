#Simulacion de una cola de atencion en un banco
class Banco:
    def __init__(self):
        self.cola=[]
    
    #Metodos o acciones de la clase
    def nuevo_Cliente(self,cliente):
        self.cola.append(cliente)
        print (f"Cliente {cliente} ha llegado al banco")

    #Metodo para atender al clinete
    def atender_Cliente(self):
        if self.cola:
            clienteAtendido=self.cola.pop(0)
            print (f"Atendiendo al cliente {clienteAtendido}")
        else:
            print("No hay clientes en la cola")

    def clientesEspera(self):
        return len(self.cola)
    

#Objetos de la clase
bancoBNB=Banco()
bancoBNB.nuevo_Cliente("Kevin Arroyo")
bancoBNB.nuevo_Cliente("Jesus")
bancoBNB.nuevo_Cliente("Jose")
bancoBNB.nuevo_Cliente("Maria")
bancoBNB.nuevo_Cliente("Ana")


bancoBNB.atender_Cliente()
print(f"Clientes esperando: {bancoBNB.clientesEspera()}")
bancoBNB.atender_Cliente()
bancoBNB.atender_Cliente()