#Clase Pila - Metodo Apilar - Desapilar push pop
#Paso 1. Crear la clase
class Pila:
    def __init__(self):
        self.pila=[] #Pila donde se guardaran los elementos 

    #Paso 2. Crear los metodos de la clase
    def push(self,plato): #push para apilar -
        self.pila.append(plato) #Agregar el plato en la pila
        print (f"Aplinado el plato:{plato}")

    def pop(self): #poop para desapilar
        if self.pila_Vacia():
            return "La pila esta vacia" 
        plato=self.pila.pop()
        print(f"Desapilando el plato:{plato} ")

    def pila_Vacia(self):
        return len(self.pila)==0
    
    def peek(self): #Ver el ultimo elemento de la pila
        if self.pila_Vacia():
            return "La pila esta vacia"
        return self.pila[-1] #devolvernos el ultimo plato apilado



pruebaPila=Pila()
pruebaPila.push(1)
pruebaPila.push(2)
pruebaPila.push(3)

print ("El ultimo plato apilado es ", pruebaPila.peek())
print("Desapilando plato ", pruebaPila.pop()) #SALIDA 3
print("Desapilando Plato ", pruebaPila.pop()) #SALIDA 2
print("Desapilando plato ",pruebaPila.pop()) #SALIDA 1
print("La pila esta vacia: ", pruebaPila.pila_Vacia()) #TRUE



colores=["rojo", "amarillo","verde","azul","cafe","lila","negro","celeste"]
#0,1,2,3,4,5
if colores:
    color=colores[3]
    print("El cuarto color es ",color)
    print ("La cantidad de colores es ", len(colores))
    print ("El ultimo color de la lista es: ",colores[-1])