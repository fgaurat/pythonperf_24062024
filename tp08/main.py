from Rectangle import Rectangle

def main():
    r = Rectangle(2,3)
    print(r)
    r.toto = 12
    
    print(r.toto)
    print(r.__dict__)

if __name__=='__main__':
    main()
