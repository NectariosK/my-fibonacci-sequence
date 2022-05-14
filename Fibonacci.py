#Fibonacci
def fibonacci(number):
	a = 0
	b = 1
	for i in range(number):
		yield a
		temp = a
		a = b 
		b = temp + b


# Fibonacci, Golden Formula
def fib( n: int) -> int:
    phi = (1.0 - sqrt(5)) / 2.0
    Phi = (1.0 + sqrt(5)) / 2.0
    return (int)(( pow(Phi, n) - pow(phi,n) ) / sqrt(5))


for x in fibonacci(20):
	print(x)

#Solving the Fibonacci using a list
'''
def fib2(number):
    a =  0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fib2(100))
'''