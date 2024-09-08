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


class Tareas:
    def __init__(self):
        self.tareasUrgentes=Pila()
        self.tareasNormales=Cola()

    #Metodos
    def agregarTarea(self,tarea,urgencia):
        if urgencia=="urgente":
            self.tareasUrgentes.apilar(tarea)
        else:
            self.tareasNormales.encolar(tarea)
    
    def procesarTarea(self):
        if not self.tareasUrgentes.es_vacia():
            return self.tareasUrgentes.desapilar()
        elif not self.tareasNormales.es_Vacia():
            return self.tareasNormales.desencolar()
        else:
            return "No hay tareas pendientes"

    def mostrarTareas(self):
        print("Tareas Urgente: ",self.tareasUrgentes.mostrar_pila())
        print("Tareas Normales: ",self.tareasNormales.mostrar_cola())

sistema=Tareas()
sistema.agregarTarea("Tarea A","urgente")
sistema.agregarTarea("Tarea B","no urgente")
sistema.agregarTarea("Tarea C","urgente")
sistema.agregarTarea("Tarea D","no urgente")
sistema.mostrarTareas()
print("Tarea procesada: ",sistema.procesarTarea())
print("Tarea procesada: ",sistema.procesarTarea())
print("Tarea procesada: ",sistema.procesarTarea())
sistema.mostrarTareas()