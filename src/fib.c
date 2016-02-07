#include <stdio.h>
#include <time.h>

int fib(int num) {
    return num < 2 ? num : fib(num-1) + fib(num-2);
}

main () {
    int test_num = 35;
    int actual;
    clock_t start, stop;
    double avg_time, total_time, counter, time_in_clock_ticks, time_in_seconds;
    for (counter = 0; counter < 10; counter++) {
        start = clock();
        actual = fib(test_num);
        stop = clock();
        time_in_clock_ticks = stop-start;
        time_in_seconds = (double)time_in_clock_ticks / (double)CLOCKS_PER_SEC;
        // printf("%f\n", time_in_seconds);
        total_time = total_time + time_in_seconds;
    }
    avg_time = total_time / (counter);
    printf("Lang:C(Clang-3.5),Result:%d,Runtime:%f\n", actual, avg_time);
}
