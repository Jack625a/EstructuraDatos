class Nodo:
    def __init__(self, valor):
        self.valor=valor
        self.izquierda=None
        self.derecha=None

#Clase para el Arbol
class Arbol:
    def __init__(self):
        self.raiz=None
    
    #Acciones del arbol (Insercion, recorrido, busqueda)
    def insertar(self,valor):
        #Si nuestro arbol esta vacio debemos asignar la raiz
        if self.raiz is None:
            self.raiz=Nodo(valor)
        else:
            #Si no esta vacio, insertamoas el nuevo nodo (recursibamente)
            self.recursivoInsercion(self.raiz,valor)
    def recursivoInsercion(self,nodo,valor):
        if valor< nodo.valor:
            #Se deberar inserat en el subarbol izquierdo
            if nodo.izquierda is None:
                nodo.izquierda=Nodo(valor)
            else:
                self.recursivoInsercion(nodo.izquierda,valor)
                #Insertar en el subarbol derecho
        else:
            if nodo.derecha is None:
                nodo.derecha=Nodo(valor)
            else:
                self.recursivoInsercion(nodo.derecha,valor)
