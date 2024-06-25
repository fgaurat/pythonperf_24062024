
class Cercle:
    
    def __init__(self, rayon=0) -> None:
        self.__rayon = rayon

    @property
    def rayon(self):
        return self.__rayon

    @rayon.setter
    def rayon(self,value):
        self.__rayon = value

    def __str__(self) -> str:
        return f"{__class__.__name__}: {self.__rayon=}"


    def __eq__(self, value: object) -> bool:
        return self.__rayon == value.__rayon