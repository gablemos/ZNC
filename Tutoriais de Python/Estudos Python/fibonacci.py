def fib(x):
	a,b = 1,1
	for i in range(x-1):
		a,b = b,a+b
	return a
print fib(5)