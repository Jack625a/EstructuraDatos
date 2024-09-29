#Convercion de un Numero Decimal a Binario
class Pila:
    def __init__(self):
        #Paso 1. Crear la pila Vacia
        self.pila=[]
    
    #Metodos o acciones de la pila
    #Apilamiento
    def push(self, residuo):
        self.pila.append(residuo)
    #Desapilamiento 
    def pop(self):
        if self.pilaVacia():
            return "La pila esta vacia"
        return self.pila.pop()
    #Verificacion de pila Vacia
    def pilaVacia(self):
        return len(self.pila)==0
    

def decimal_binario(numero):
    pila=Pila()
    while numero>0:
        residuo=numero%2
        pila.push(residuo)
        numero=numero//2
    binario=''
    while not pila.pilaVacia():
        binario+= str(pila.pop())
    return binario

#Ejemplo de uso de la funcion
numero_decimal=int(input("Ingrese un numero decimal: "))
resultado=decimal_binario(numero_decimal)
print(f"El numero {numero_decimal} en base 10 es igual a {resultado} en base 2")
