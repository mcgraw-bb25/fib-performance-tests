import time
from ctypes import cdll

lib = cdll.LoadLibrary("lib/rust_ext/libfib_lib.so")

if __name__ == "__main__":
    test_n = 35
    total_time = 0.0
    for i in range(0,10):
        t = time.time()
        actual = lib.fib(test_n)
        t = time.time()-t
        ## print(t)
        total_time = total_time + t
    avg_time = total_time / 10.0
    print ("Lang:rustyPython3,Result:%s,Runtime:%s" % (actual,avg_time))
