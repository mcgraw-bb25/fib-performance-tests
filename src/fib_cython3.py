from lib.cython_ext import juliafib
import time

if __name__ == "__main__":
    test_n = 35
    total_time = 0.0
    for i in range(0,10):
        t = time.time()
        actual = juliafib.julia_fib(test_n)
        t = time.time()-t
        ## print (t)
        total_time = total_time + t
    avg_time = total_time / 10.0
    print ("Lang:Cython3,Result:%s,Runtime:%s" % (actual,avg_time))
