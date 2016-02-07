require "time"
require "ffi"

module Fib
	extend FFI::Library
	ffi_lib "lib/rust_ext/libfib_lib.so"
	attach_function :fib, [ :int ], :int
end

test_n = 35
total_time = 0.0
actual = 0
10.times do
    t = Time.new.to_f
    actual = Fib.fib(test_n)
    t = Time.new.to_f - t
    ## puts "#{t}"
    total_time = total_time + t
end
avg_time = total_time / 10.0
puts "Lang:rustyRuby,Result:#{actual},Runtime:#{avg_time}"

