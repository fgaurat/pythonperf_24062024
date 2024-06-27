from Carre import Carre
from Cercle import Cercle

def main():
    c = Carre(2)
    c1 = Carre(2)
    ce = Cercle(2)

    if c==c1:
        print("ok")
    else:
        print("ko")

    print(c)
    print(c.surface)
    c.cote= 5
    print(c.surface)
    print(ce.surface)


if __name__=='__main__':
    main()

