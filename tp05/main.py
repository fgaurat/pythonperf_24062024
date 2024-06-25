from Carre import Carre

def main():
    c = Carre(2)
    c1 = Carre(2)
    

    if c==c1:
        print("ok")
    else:
        print("ko")

    print(c)
    print(c.surface)
    c.cote= 5
    print(c.surface)


if __name__=='__main__':
    main()

