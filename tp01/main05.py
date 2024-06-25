def mult2(i):
    return i*2

def main():
    l= [10,20,30,40,50]
    l2=[]

    for i in l:
        l2.append(i*2)
    
    print(l2)
    
    l2 = [i *2 for i in l]
    print(l2)

    l_s = ["   toto   ","   tutu", "tata   "]
    l3 = [s.strip() for s in l_s]
    print(l_s)
    print(l3)

    l= [10,20,30,40,50]

    # l2 = list(map(mult2,l))
    l2 = list(map(lambda i:i*2,l))
    print(l2)

    


if __name__=='__main__':
    main()
