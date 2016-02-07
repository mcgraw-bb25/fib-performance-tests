function fib(n) {
    if (n < 2) { return n; }
    return fib(n-1) + fib(n-2);
}

var test_n = 35;
var total_time = 0.0;
var actual = 0;
var t = Date.now();

for (var i = 0; i < 20; i++){
	t = Date.now();
	actual = fib(test_n);
	t = Date.now() - t;
	total_time = total_time + t;
}
var avg_time = (total_time/1000)/i;
var output = "Lang:JavaScript(Node),Result:".concat(actual);
output = output.concat(",TotalTime:").concat(total_time);
output = output.concat(",Loops:").concat(i);
output = output.concat(",Runtime:").concat(avg_time);
console.log(output);
