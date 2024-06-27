
from typing import Any


class Singleton(type):

    __instance = None
    
    def __call__(self,*args,**kwargs): 
        if self.__instance is None:
            self.__instance = super().__call__(*args,**kwargs)
        else:
            self.__instance.__init__(*args,**kwargs)
        return self.__instance 

class RectangleMetaSingleton(metaclass=Singleton):

    __cpt=0    
    
    def __init__(self,longueur=0,largeur=0) -> None:
        self.__longueur=longueur
        self.__largeur=largeur
        RectangleMetaSingleton.__cpt+=1

    @classmethod
    def buildFromStr(cls,value):
        longueur,largeur = [int(i) for i in value.split(",")]
        return cls(longueur,largeur)
    
    @staticmethod
    def get_cpt():
        return RectangleMetaSingleton.__cpt
    
    
    @property
    def longueur(self):
        return self.__longueur
    @property
    def largeur(self):
        return self.__largeur
    
    @longueur.setter
    def longueur(self,value):
        self.__longueur = value
    
    @largeur.setter
    def set_largeur(self,value):
        self.__largeur = value

    @property
    def surface(self):
        return self.__largeur*self.__longueur

    def __str__(self) -> str:
        return f"{__class__.__name__}: {self.__longueur=},{self.__largeur=}"
    

    # longueur = property(fget=get_longueur,fset=set_longueur,doc="Longueur property")
    # largeur = property(get_largeur,set_largeur,doc="Largeur property")
    # surface = property(get_surface,doc="Surface property")