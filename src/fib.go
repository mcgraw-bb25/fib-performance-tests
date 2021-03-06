package main

import (
    "fmt"
    "time"
)

func fib(n int) int {
    if n < 2 {
        return n
    }
    return fib(n-1) + fib(n-2)
}

func main() {

    var test_n int = 35
    var result int
    var total_time float64
    var avg_time float64
    var counter float64

    for i := 0; i < 20; i++ {
        start := time.Now()
        result = fib(test_n)
        stop := time.Now()
        total_time = total_time + float64(stop.Sub(start))/1E9
        // fmt.Printf("%v\n", float64(stop.Sub(start))/1E9)
        counter = float64(i)
    }
    avg_time = (total_time/(counter+1.0))
    fmt.Printf("Lang:Go,Results:%v,TotalTime:%v,Loops:%v,Runtime:%v\n",result,total_time,counter+1,avg_time)
}
