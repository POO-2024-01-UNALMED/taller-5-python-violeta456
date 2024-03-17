from gestion.zona import Zona
from mamifero import Mamifero
from ave import Ave
from pez import Pez
from anfibio import Anfibio
from reptil import Reptil
class Animal():
    totalAnimales=0

    def __init__(self,nombre=None,edad=0,habitat=None,genero=None,zonas=None):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        if zonas==None:
            self._zonas=[]
        Animal.totalAnimales+=1
    def movimiento():
        return "desplazarce"
    
    @classmethod
    def totalPorTipo():
        return "Mamiferos:",Mamifero.cantidadMamiferos(),"\n", "Aves:",Ave.cantidadAves(),"\n","Reptiles:",Reptil.cantidadReptiles(),"\n","Peces:",Pez.cantidadPeces(),"\n","Anfibios:",Anfibio.cantidadAnfibios()
    def toString(self):
        if self._zonas!=None:
            return "Mi nombre es",self._nombre,"tengo una edad de",self._edad,"habito en",self._habitat,"y mi genero es",self._genero,"la zona en la que me ubico es",self._zonas.getNombre(),"en el",self._zonas.getZoo()
        else:
            return "Mi nombre es",self._nombre,"tengo una edad de",self._edad,"habito en",self._habitat,"y mi genero es",self._genero
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre=nombre
    def getEdad(self):
        return self._edad
    def setEdad(self, edad):
        self._edad=edad
    def getHabitat(self):
        return self._habitat
    def setHabitat(self, habitat):
        self._habitat=habitat
    def getGenero(self):
        return self._genero
    def setGenero (self,genero):
        self._genero=genero   
    def getZonas(self):
        return self._zonas
    def setZonas(self, zonas):
        self._zonas=zonas