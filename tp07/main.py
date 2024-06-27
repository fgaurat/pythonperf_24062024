from typing import Any
from Rectangle import Rectangle
from RectangleSingleton import RectangleSingleton
from RectangleSingletonDeco import RectangleSingletonDeco
from RectangleMetaSingleton import RectangleMetaSingleton

class TheClass:

    def __new__(cls):
        print("def __new__(cls)")
        self = super().__new__(cls)
        return self


    def __init__(self):
        print("def __init__(self)")

    def __call__(self) -> Any:
        print("def __call__(self) -> Any")

def main():
    r = Rectangle(1,2)
    r1 = Rectangle(1,2)
    
    print(hex(id(r)))
    print(hex(id(r1)))

    t = TheClass()
    t()
    print('-'*50)
    r = RectangleSingleton(2,5)
    r1 = RectangleSingleton(85,59)
    print(hex(id(r)))
    print(hex(id(r1)))   
    print(r)
    print(r1)
    print(50*'-')
    r =RectangleSingletonDeco(2,3)    
    r1 =RectangleSingletonDeco(2,3)    
    print(hex(id(r)))
    print(hex(id(r1)))

    r = Rectangle(1,2)
    print(type(r))
    print(type(Rectangle))
    
    r = RectangleMetaSingleton(1,2)
    r1 = RectangleMetaSingleton(1,2)
    print(hex(id(r)))
    print(hex(id(r1)))



def main_meta():
    a = 2
    print(a)
    print(type(a))
    print(type(int))


if __name__=='__main__':
    main_meta()
