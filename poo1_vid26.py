
class Coche():
    
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    """ Metodo comportamientos, de un coche, arrancar, parar, derrapar, lo que puede hacer un coche """

    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos
        
        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en  marcha"
        
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo no podemos arrancar"
        
        else:
            return "El coche esta parado"
            

    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)
        
    
    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite="ok"
        self.puertas="cerradas"
        
        if(self.aceite=="ok" and self.gasolina=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False 
        
        

"""Instanciar una clase, la clase coche"""
miCoche=Coche()

"""  Nomenclatura del punto = Nombre_del_objeto . propiedad """



print(miCoche.arrancar(True))

miCoche.estado()

print("----------------------------------  A continiacion creamos el segundo objeto.  ----------------------------------")

micoche2=Coche()



print(micoche2.arrancar(False))

micoche2.estado()


