class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
	
    """ Metodos o comportamientos, de un coche, arrancar, parar, derrapar, lo que puede hacer un coche """

    def arrancar(self):
        self.enmarcha=True

    def estado(self):
        if(self.enmarcha==True):
            return "El coche esta en  marcha"
        else:
            return "El coche esta parado"

"""Instanciar una clase, la clase coche"""
miCoche=Coche()

"""  Nomenclatura del punto = Nombre_del_objeto . propiedad """

print("El largo del coche es: ", miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, "ruedas")
miCoche.arrancar()

print(miCoche.estado())
