require "time"

def fib(n)
    if n < 2
        return n
    end
    return fib(n-1) + fib(n-2)
end

test_n = 35
total_time = 0.0
actual = 0
10.times do
    t = Time.new.to_f
    actual = fib(test_n)
    t = Time.new.to_f - t
    ## puts "#{t}"
    total_time = total_time + t
end
avg_time = total_time / 10.0
puts "Lang:Ruby,Result:#{actual},Runtime:#{avg_time}"

