class Cola:
    def __init__(self):
        self.datos=[]

    #Metodos
    def encolar(self,dato):
        self.datos.append(dato)
    
    def desencolar(self):
        if not self.es_Vacia():
            return self.datos.pop(0)
        else:
            return None

    def es_Vacia(self):
        return len(self.datos)==0
    
    def mostrar_cola(self):
        print(self.datos)

cola=Cola()
cola.encolar(5)
cola.encolar(15)
cola.encolar(25)
cola.encolar(35)
cola.mostrar_cola()
print("Elemento desencolado: ",cola.desencolar())
cola.mostrar_cola()