
class Coche():
    
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    """ Metodo comportamientos, de un coche, arrancar, parar, derrapar, lo que puede hacer un coche """

    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha==True):
            return "El coche esta en  marcha"
        else:
            return "El coche esta parado"
            

    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)
        
        

"""Instanciar una clase, la clase coche"""
miCoche=Coche()

"""  Nomenclatura del punto = Nombre_del_objeto . propiedad """



print(miCoche.arrancar(True))

miCoche.estado()

print("----------------------------------  A continiacion creamos el segundo objeto.  ----------------------------------")

micoche2=Coche()



print(micoche2.arrancar(False))

micoche2.ruedas=2

micoche2.estado()


