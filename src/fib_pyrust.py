import time
from ctypes import cdll

lib = cdll.LoadLibrary("lib/rust_ext/libfib_lib.so")

if __name__ == "__main__":
    test_n = 35
    total_time = 0.0
    for i in range(0,20):
        t = time.time()
        actual = lib.fib(test_n)
        t = time.time()-t
        ## print(t)
        total_time = total_time + t
    avg_time = total_time / ((i + 1.0) * 1.0)
    print ("Lang:rustyPython3,TotalTime:%s,Loops:%s,Result:%s,Runtime:%s" % (actual,total_time,i+1,avg_time))
