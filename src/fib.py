import time

def julia_fib(n):
    if n<2:
        return n
    return julia_fib(n-1)+julia_fib(n-2)

if __name__ == "__main__":
    test_n = 35
    total_time = 0.0
    for i in range(0,10):
        t = time.time()
        actual = julia_fib(test_n)
        t = time.time()-t
        ## print(t)
        total_time = total_time + t
    avg_time = total_time / 10.0
    print ("Lang:Python3(Native),Result:%s,Runtime:%s" % (actual,avg_time))
