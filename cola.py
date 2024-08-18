class Cola:
    def __init__(self):
        #Parametros
        self.personas=[]

    #Metodos de la clase (Encolar- Desencolar - Cola Vacia)
    def colaVacia(self):
        return len(self.personas)==0
    
    def encolar(self,persona):
        self.personas.append(persona)
    
    def desencolar(self):
        if not self.colaVacia():
            return self.personas.pop(0)
        else:
            return "La cola esta vacia"
    def personaAlFrente(self):
        if not self.colaVacia():
            return self.personas[0]
        else:
            return "Cola esta vacia"

#Ejemplo de uso para personas que realizan su pago del producto comprado
cola=Cola()
cola.encolar("Kevin Arroyo")
cola.encolar("Juan Perez")
cola.encolar("Carlos Villegas")
cola.encolar("Jesus")
cola.encolar("Mateo")
print("Persona al frente para ser atendida: ",cola.personaAlFrente())
print(cola.personaAlFrente(), "A sido antendido... Gracias por su compra ", cola.desencolar())
print("Persona al frente para ser atendida: ",cola.personaAlFrente())
