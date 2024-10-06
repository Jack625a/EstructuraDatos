# Paso 1. Definición de la clase Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Paso 2. Definir la clase Árbol 
class ArbolExpresiones:
    def __init__(self):
        self.raiz = None

    # Paso 3. Definir los métodos de la clase
    def construirArbol(self, expresion):
        pila = []
        for caracter in expresion:
            if caracter.isdigit():  # Si el caracter analizado es un número debemos crear un nodo hoja
                nodo = Nodo(int(caracter))
                pila.append(nodo)
            else:  # Si no es un número, sacamos dos nodos de la pila y creamos el nodo operador
                nodo = Nodo(caracter)
                nodo.derecha = pila.pop()  # El segundo nodo sale primero (derecha)
                nodo.izquierda = pila.pop()  # El primer nodo sale después (izquierda)
                pila.append(nodo)  # Volvemos a agregar el nodo operador
        # La raíz del árbol debe ser el único nodo restante en la pila
        self.raiz = pila.pop()

    # Método para evaluar el resultado
    def evaluar(self, nodo):
        # Si el nodo es una hoja numérica, devolver el valor
        if nodo.izquierda is None and nodo.derecha is None:
            return nodo.valor
        
        # Evaluar las subramas de la izquierda y de la derecha
        valor_izquierda = self.evaluar(nodo.izquierda)
        valor_derecha = self.evaluar(nodo.derecha)

        if nodo.valor == '+':
            return valor_izquierda + valor_derecha
        elif nodo.valor == '-':
            return valor_izquierda - valor_derecha
        elif nodo.valor == '*':
            return valor_izquierda * valor_derecha
        elif nodo.valor == '/':
            return valor_izquierda / valor_derecha

    # Método para mostrar la expresión en formato infijo
    def mostrar(self, nodo):
        if nodo is not None:
            if nodo.izquierda or nodo.derecha:
                print("(", end="")
            self.mostrar(nodo.izquierda)
            print(nodo.valor, end="")
            self.mostrar(nodo.derecha)
            if nodo.izquierda or nodo.derecha:
                print(")", end="")

# Función principal para manejar el árbol
def inicio():
    arbol = ArbolExpresiones()
    expresion = "81+95/*15*+"
    arbol.construirArbol(expresion)

    print("Expresión en formato infijo:")
    arbol.mostrar(arbol.raiz)
    print("\n")

    resultado = arbol.evaluar(arbol.raiz)
    print(f"El resultado de la expresión es: {resultado}")

if __name__ == "__main__":
    inicio()
