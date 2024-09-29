#Ejercicio 1. Crear un programa para invertir un cadena de carteres
class Pila:
    def __init__(self):
        self.pila=[]
    
    def push(self,elemento):
        self.pila.append(elemento)
    
    def pop(self):
        if self.pilaVacia():
            return "La pila esta vacia "
        return self.pila.pop()
    
    def pilaVacia(self):
        return len(self.pila)==0
    

#Funcion para invertir la cadena de caracteres
def invertir(cadena):
    pila=Pila()
    for caracter in cadena:
        pila.push(caracter)
    cadena_invertida=''
    while not pila.pilaVacia():
        cadena_invertida +=pila.pop()
    return cadena_invertida


cadena=input("Ingrese la cadena de caracteres: ")
resultado=invertir(cadena)
print(f"Cadena invertida: {resultado}")