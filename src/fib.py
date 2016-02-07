import time

def julia_fib(n):
    if n<2:
        return n
    return julia_fib(n-1)+julia_fib(n-2)

if __name__ == "__main__":
    test_n = 35
    total_time = 0.0
    for i in range(0,20):
        t = time.time()
        actual = julia_fib(test_n)
        t = time.time()-t
        ## print(t)
        total_time = total_time + t
    avg_time = total_time / ((i + 1) * 1.0)
    print ("Lang:Python3(Native),Result:%s,TotalTime:%s,Loops:%s,Runtime:%s" % (actual,total_time,i,avg_time))
