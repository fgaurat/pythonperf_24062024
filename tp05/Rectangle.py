class Rectangle:

    __cpt=0    
    
    def __init__(self,longueur=0,largeur=0) -> None:
        self.__longueur=longueur
        self.__largeur=largeur
        Rectangle.__cpt+=1

    @classmethod
    def buildFromStr(cls,value):
        longueur,largeur = [int(i) for i in value.split(",")]
        return cls(longueur,largeur)
    
    @staticmethod
    def get_cpt():
        return Rectangle.__cpt
    
    
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
    def largeur(self,value):
        self.__largeur = value

    @property
    def surface(self):
        return self.__largeur*self.__longueur

    def __str__(self) -> str:
        return f"{__class__.__name__}: {self.__longueur=},{self.__largeur=}"
    

    # longueur = property(fget=get_longueur,fset=set_longueur,doc="Longueur property")
    # largeur = property(get_largeur,set_largeur,doc="Largeur property")
    # surface = property(get_surface,doc="Surface property")