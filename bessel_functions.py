import math
def BesselJ(n,x,iteration_limit=100):
	j = 0
	for i in range(0,iteration_limit):
		j += (-1) ** i / (2 ** (2*i+n) * factorial(i) * factorial(n+i)) * x ** (2*i+n)
	return j

def BesselY0(x,iteration_limit=100):
	term1 = (math.log(0.5 * x) + euler_mascheroni(iteration_limit)) * BesselJ(0,x,iteration_limit)
	term2 = 0
	for k in range(1,iteration_limit+1):
		term2 += (-1) ** (k+1) * harmonic_number(k) * (0.25 * x * x) ** k / (factorial(k) ** 2)
	y0 = (term1 + term2) * 2 / math.pi
	return y0

def euler_mascheroni(iteration_limit=100):
	return harmonic_number(iteration_limit) - math.log(iteration_limit)

def harmonic_number(n):
	s = 0
	for k in range(1,n+1):
		s += k ** -1
	return s

def factorial(n):
	if n < 0:
		return -1
	if n < 2:
		return 1
	p = n
	while n > 1:
		n -= 1
		p *= n
	return p

print(BesselY0(5,iteration_limit=98))