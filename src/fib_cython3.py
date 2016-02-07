from lib.cython_ext import juliafib
import time

if __name__ == "__main__":
    test_n = 35
    total_time = 0.0
    for i in range(0,20):
        t = time.time()
        actual = juliafib.julia_fib(test_n)
        t = time.time()-t
        ## print (t)
        total_time = total_time + t
    avg_time = total_time / ((i + 1.0) * 1.0)
    print ("Lang:Cython3,Result:%s,TotalTime:%s,Loops:%s,Runtime:%s" % (actual,total_time,i+1,avg_time))
