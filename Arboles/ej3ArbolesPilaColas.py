#Ejercicio 1. Organizador de Tareas
#Arboles. Pilas. Colas

#Paso 1. Definir la estructura del Arbol de tareas
class Tarea:
    def __init__(self, nombre):
        self.nombre=nombre
        self.subtareas=[]

    def agregarSubtarea(self,subtarea):
        self.subtareas.append(subtarea)

#Paso 2. Crear el recorrido con pilas
def recorrido(tareaPrincipal):
    if tareaPrincipal is None:
        return
    pila=[]
    pila.append(tareaPrincipal)

    while pila:
        tareaActual=pila.pop()
        print(tareaActual.nombre, 'se ha completado')

        for subtarea in reversed(tareaActual.subtareas):
            pila.append(subtarea)

#Paso 3. Crear el recorrico con colas
from collections import deque

def recorridoCola(tareaPrincipal):
    if tareaPrincipal is None:
        return
    cola=deque()
    cola.append(tareaPrincipal)

    while cola:
        tareaActual=cola.popleft()
        print(tareaActual.nombre, 'se ha completado')

        for subtarea in tareaActual.subtareas:
            cola.append(subtarea)

#Paso 4. Probar los recorricos

#Tareas Principales y las subtareas
tarea1=Tarea('Planificacion')
tarea2=Tarea('Diseño')
tarea3=Tarea('Desarrollo')
tarea4=Tarea('UI')
tarea5=Tarea('UX')
tarea6=Tarea('Testeo') 

tarea1.agregarSubtarea(tarea2)
tarea1.agregarSubtarea(tarea3)
tarea2.agregarSubtarea(tarea4)
tarea2.agregarSubtarea(tarea5)
tarea3.agregarSubtarea(tarea6)


#Recorridos
print('Recorrido por Pilas')
recorrido(tarea1)


print('Recorrido por Colas')
recorridoCola(tarea1)