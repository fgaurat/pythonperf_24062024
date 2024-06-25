from pprint import pprint
import copy
def main():
    l= [10,20,30,40,50]
    l[0] = 1000
    print(l)
    print(l[-1])
    print(l[1:4]) # [1:4[

    # l1 = l[:]
    l1 = l.copy()
    # l1 = copy.copy(l1)
    l[0]=12
    print(l)
    print(l1)

    l2 = [
        [10,20,30],
        [40,50,60],
        [70,80,90],
    ]
    l3 = copy.deepcopy(l2)

    l2[1][1] = 5000
    print(l2)
    print(l3)





if __name__=='__main__':
    main()
