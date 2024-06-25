


def divi(a,b):
    return a/b

def call_divi(a,b):
    try:
        print("open file")
        r = divi(a,b)
    finally:    
        print("close file")
   
    return r

def main():
    try:
        a = 2
        b= 0
        c = call_divi(a,b)
    except ValueError as e:
        print("ValueError",e)
    except ZeroDivisionError as e:
        print("ZeroDivisionError",e)
    except Exception as e:
        print("Exception",e)


    print("la suite du code")


if __name__=='__main__':
    main()
