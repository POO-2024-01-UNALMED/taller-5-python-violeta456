from zona import Zona
class Zoologico():
    
    def __init__(self,nombre=None, ubicacion=None,zonas=None):
        self._nombre=nombre
        self._ubicacion=ubicacion
        if zonas==None:
            self._zonas=[]
    
    def agregarZonas(self,zona):
        self._zonas.append(zona)
    
    def cantidadTotalAnimales(self):
        cantidad=0
        for i in self._zonas:
            cantidad+= i.cantidadAnimales()
        return cantidad
    
    def __str__(self):
        return self._nombre

    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre=nombre
    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self, ubicacion):
        self._ubicacion=ubicacion
    def getZonas(self):
        return self._zonas
    def setAnimales(self, zonas):
        self._zonas=zonas   
