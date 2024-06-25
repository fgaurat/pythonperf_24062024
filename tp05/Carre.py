from Rectangle import Rectangle

class Carre(Rectangle):
    
    def __init__(self, cote=0) -> None:
        super().__init__(cote, cote)
        self.__cote = cote

    @property
    def cote(self):
        return self.__cote

    @cote.setter
    def cote(self,value):
        self.__cote = value
        self.longueur = value
        self.largeur = value

    def __str__(self) -> str:
        return f"{__class__.__name__}: {self.__cote=}"


    def __eq__(self, value: object) -> bool:
        return self.__cote == value.__cote