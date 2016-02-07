function fib(n) {
    if (n < 2) { return n; }
    return fib(n-1) + fib(n-2);
}

var test_n = 35;
var total_time = 0.0;
var actual = 0;
var t = Date.now();

for (var i = 0; i < 10; i++){
	t = Date.now();
	actual = fib(test_n);
	t = Date.now() - t;
	total_time = total_time + t;
}
var avg_time = (total_time/1000)/10.0;
var output = "Lang:JavaScript(Node),Result:";
output = output.concat(actual);
output = output.concat(",Runtime:");
output = output.concat(avg_time);
console.log(output);
