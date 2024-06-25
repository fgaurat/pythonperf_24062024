def make_incrementor(inc):

    def f(value):
        return value+inc

    return f


def main():
    do_inc = make_incrementor(2)

    r = do_inc(5) # 7
    r1 = do_inc(2) # 2
    r2 = do_inc(15) # 17

if __name__=='__main__':
    main()
