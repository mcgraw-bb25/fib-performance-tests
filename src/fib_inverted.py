import time

def memoizer(cache, n):
    for number in range(0,n+1):
        if n not in cache:
            cache = julia_fib(cache, number)
    fib = cache[n]
    return fib

def julia_fib(cache, n):
    if n not in cache:
        if n<2:
            cache[n] = n
            return cache
        cache[n] = cache[n-1] + cache[n-2]
        return cache
    else:
        return cache

if __name__ == "__main__":
    test_n = 35
    total_time = 0.0
    for i in range(0,20):
        cache = {}
        t = time.time()
        actual = memoizer(cache, test_n)
        t = time.time()-t
        ## print(t)
        total_time = total_time + t
    avg_time = total_time / ((i + 1.0) * 1.0)
    print ("Lang:Python3(Inverted),Result:%s,TotalTime:%s,Loops:%s,Runtime:%s" % (actual,total_time,i+1,avg_time))
