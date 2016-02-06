using Dates

function get_time(given_time)
	hour_ms = hour(given_time)
	minutes_ms = minute(given_time)
	seconds_ms  = second(given_time)
	ms_ms = millisecond(given_time)
	time_ms = (hour_ms * 60 * 60 * 1000)
	time_ms = time_ms + (minutes_ms * 60 * 1000)
	time_ms = time_ms + (seconds_ms * 1000)
	time_ms = time_ms + ms_ms
	return time_ms
end

function fib(n)
	if n < 2
		return n
	else
		fib(n-1) + fib(n-2)
	end
end

actual = 0
total_time = 0

for i in 1:10
	start = now()
	actual = fib(35)
	stop = now()
	start_time = get_time(start)
	stop_time = get_time(stop)
	run_time = (Float64(stop_time) - Float64(start_time))
	print("$run_time milliseconds\n")
	total_time = total_time + run_time
end

avg_time = (total_time / 1000) / 10

print("Lang:Julia,Result:$actual,Runtime:$avg_time\n")
