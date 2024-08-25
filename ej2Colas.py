#Simulacion de una Impresora
class Impresora:
    def __init__(self):
        self.cola=[]
    
    #Metodos o acciones  de la clase
    def agregarDocumento(self,nombre,paginas):
        documento={"nombre":nombre,"paginas":paginas}
        self.cola.append(documento)
        print(f"Documentos '{nombre} agregado a la cola de impresion con la cantidad de paginas {paginas}'")
    
    def imprimir(self):
        while self.cola:
            documento=self.cola.pop(0)
            print(f"Imprimiendo el documento '{documento['nombre']}'")
        print("TODOS LOS DOCUMETNOS HAN SIDO IMPRESOS")
    
    def colaEsperaImpresion(self):
        return len(self.cola)
    

#Objetos de la clase
impresaHP=Impresora()
impresaHP.agregarDocumento("Documento1",20)
impresaHP.agregarDocumento("Documento2",10)
impresaHP.agregarDocumento("Documento3",5)
impresaHP.agregarDocumento("Documento4",2)
impresaHP.agregarDocumento("Documento5",30)

impresaHP.imprimir()


