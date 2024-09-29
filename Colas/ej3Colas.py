#Simulacion de un sistema de soporte tecnico con tiempos de atencion 
class SoporteTecnico:
    def __init__(self):
        self.cola=[]
    #Metodos o acciones
    def solicitudSoporte(self,usuario,tiempo):
        solicitud = {"usuario": usuario, "tiempo": tiempo}
        self.cola.append(solicitud)
        print(f"Solucitud registrada del usuario {usuario}")
    
    def atenderSolicitud(self):
        if not self.cola:
            print("No hay solicitudes que deban ser atendidas")
        else:
            solicitud=self.cola.pop(0)
            print(f"Atendiendo la solicitud {solicitud['usuario']} que tardara un total de {solicitud['tiempo']} minutos")
    
    def tiempoTotalEspera(self):
        total=sum(solicitud["tiempo"] for solicitud in self.cola)
        print(f"Tiempo total de espera para la solucion a las solicitudes totales {total} minutos" )
        return total
    

soporte=SoporteTecnico()
soporte.solicitudSoporte('Usuario1', 15)
soporte.solicitudSoporte("Jesus",180)
soporte.solicitudSoporte("Juan",30)
soporte.solicitudSoporte("Ana",60)

soporte.tiempoTotalEspera()
soporte.atenderSolicitud()
soporte.tiempoTotalEspera()
soporte.atenderSolicitud()
soporte.tiempoTotalEspera()

