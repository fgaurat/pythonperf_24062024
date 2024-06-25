def add(*l)->int:
    """
    calc sum from l
    """
    print(l)
    r = 0
    for i in l:
        r+=i
    return r



def hello(**params):
    print(params)
    print("Bonjour",params['name'],params['firstname'])

def main():
    l= [10,20,30,40,50]
    
    r = add(*l)
    print(r) # 150

    r1 = add(10,20,30,40,50)
    print(r1) # 150

    # l= [10,20,30]
    # a,b,c = l
    a,b,*c=0,1,2,3,4,5,6,7
    print(a)
    print(b)
    print(c)

    hello(name="GAURAT",firstname="Fred")
    info = {
        'name':"GAURAT",
        'firstname':"Fred"
    }
    # hello(name="GAURAT",firstname="Fred")
    hello(**info)

    s = "Bonjour {name} {firstname}".format(**info)
    print(s)


if __name__=='__main__':
    main()
