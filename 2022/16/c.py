from functools import cache

@cache
def factorial(x:int):
	if x == 0:
		return 1
	return x * factorial(x-1)

def comb(n, r):
	return factorial(n)/(factorial(r)*factorial(n-r))

sum = 0
for i in range(1, 16):
	sum += comb(15, i)

print(sum)