import sys

def main():
    print("getrefcount",sys.getrefcount(45898787984))
    a=2
    c=45898787984
    print("getrefcount",sys.getrefcount(45898787984))
    b=2
    print(a)
    print(id(a))
    
    print(hex(id(a)))
    print(hex(id(b)))
    a = 3
    print(hex(id(a)))
    print(hex(id(b)))
    print("getrefcount",sys.getrefcount(2))


    s = "toto"
    #s[0] = 'T'
    print('T'+s[1:])

if __name__=='__main__':
    main()
