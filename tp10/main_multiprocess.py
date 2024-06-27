import os
import time
from multiprocessing import Pool


def f(x):
    start = time.time()
    t = 10
    while time.time()-start < t:
        pass
    return x*x


def main():
    print(os.cpu_count())
    with Pool(2) as p:
        print(p.map(f, range(30)))



if __name__=='__main__':
    main()
