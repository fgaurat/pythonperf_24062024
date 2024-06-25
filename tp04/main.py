from Rectangle import Rectangle
from DataRectangle import DataRectangle


def main():
     r = Rectangle(longueur=5,largeur=2)
     r1 = DataRectangle(2,3)
     print(r.longueur)
     print(r.largeur)
     print(r.surface)
     print(r1.longueur)
     print(r1.largeur)
     print(r1.surface)

def oldmain():
    # r = Rectangle()
    r = Rectangle(longueur=5,largeur=2)
    r1 = Rectangle(longueur=15,largeur=25)
    r2 = Rectangle(15,25)
    r3 = Rectangle.buildFromStr("15,25")


    print(r.get_longueur()) # 5
    print(r.get_largeur()) # 2


    r.set_longueur(12)
    print(r.get_longueur()) # 12
    print(r.longueur) # 12
    print(r.get_surface()) # 24


    s = str(r)
    print(s)

    # print(Rectangle.__cpt)




    print(Rectangle.get_cpt())
    print(r.get_cpt())
    print(r3.get_surface())

    print(r.longueur)
    r.longueur = 452
    print(r.longueur)
    print(r.surface)

if __name__=='__main__':
    main()
