public class fib {
    public static int thefibber(int number) {
        if (number < 2)
            return number;
        else
            return thefibber(number - 1) + thefibber(number - 2);
    }
    public static void main(String[] args) {
        int test_num = 35;
        int actual = 0;
        long start, stop; // clocks
        double avg_time;
        long total_time, run_time, counter;
        total_time = 0;
        for (counter = 0; counter < 10; counter++) {
            start = System.nanoTime();
            actual = thefibber(test_num);
            stop = System.nanoTime();
            run_time = stop - start;
            System.out.println(run_time + " nanoseconds");
            total_time = total_time + run_time;
        }
        avg_time = total_time / counter;
        System.out.println("Lang:Java,Result:" + actual + ",Runtime:" + avg_time/(double)1E9);
    }
}