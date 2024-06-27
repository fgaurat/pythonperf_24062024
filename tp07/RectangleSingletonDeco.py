

def singleton(cls):
    instances = None
    
    def wrapper(*args,**kwargs):
        nonlocal instances
        if instances is None:
            instances = cls(*args,**kwargs)
        return instances

    return wrapper


@singleton
class RectangleSingletonDeco:

    
    def __init__(self,longueur=0,largeur=0) -> None:
        self.__longueur=longueur
        self.__largeur=largeur

    @classmethod
    def buildFromStr(cls,value):
        longueur,largeur = [int(i) for i in value.split(",")]
        return cls(longueur,largeur)
    
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