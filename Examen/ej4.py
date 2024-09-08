#pila
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


def balanceo(cadena):
    pila=Pila()
    caracteres={
        ')':'(',
        '}':'{',
        ']':'['
    }
    for char in cadena:
        if char in '({[':
            pila.apilar(char)
        elif char in ')}]':
            if pila.es_vacia() or pila.desapilar() !=caracteres[char]:
                return False
    return pila.es_vacia()


#eJERCIO PRUEBA
# "([])"
# "([)]"
# "({[]})"
cadenas=["([])","([)]","({[]})"]
for cadena in cadenas:
    print(f"La cadena '{cadena}' esta balanceada: {balanceo(cadena)}")