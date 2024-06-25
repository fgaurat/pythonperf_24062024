

def do_log(filename):
    def wrapper_func(func):
    
        def wrapper(*args,**kwargs):
            print(f"LOG to {filename}",args,kwargs)
            r = func(*args)
            print(f"LOG to {filename} RETURN",r)
            return r
        return wrapper
    return wrapper_func


@do_log("theFile.log")
def say_hello(name):
    return f"Hello {name}"

def main():
    
    h = say_hello("Fred")
    print(h)

if __name__=='__main__':
    main()
