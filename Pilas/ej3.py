#Evaluar una expresion Postfija
#Crear la pila vacia
#Hacer un recorrido a cada elemento de la expresion
#Si el elemento es un operando (numero), apilamos
#Si el elemento es un operador, desapilamos 
class Pila:
    def __init__(self):
        self.pila=[]
    #metodos
    def pilaVacia(self):
        return len(self.pila)==0
    #apilar
    def push(self, elemento):
        self.pila.append(elemento)
    #desapilar
    def pop(self):
        if self.pilaVacia():
            return "La pila esta vacia"
        return self.pila.pop()
    
def postfija(expresion):
    pila=Pila()
    for char in expresion.split():
        if char.isdigit():
            pila.push(int(char))
        else:
            op2=pila.pop()
            op1=pila.pop()
            if char =='+':
                pila.push(op1+op2)
            elif char=='-':
                pila.push(op1-op2)
            elif char=='*':
                pila.push(op1*op2)
            elif char=='/':
                pila.push(op1/op2)
    return pila.pop()

#Ejemplo
expresion=" 3 4 + 2 *"
resultado=postfija(expresion)
print(f"Resultado de la expresion: {resultado}")


