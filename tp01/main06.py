from collections import deque

def main():
    l= [10,20,30,40,50]
    print(l)
    l.append(60)
    print(l)
    the_last = l.pop()
    print(l)
    print(the_last)

    l.insert(0,0)
    print(l)
    the_first = l.pop(0)
    print(l)
    print(the_first)

    d = deque(l)
    d.appendleft(0)
    print(d)


if __name__=='__main__':
    main()
