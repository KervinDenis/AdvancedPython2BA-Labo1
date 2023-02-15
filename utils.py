import math as math
from scipy import integrate as itg

def fact(n):
    if n < 0 : 
        raise ValueError()
    if n == 0 :
        return 1
    fa = 1
    for i in range(n, 1, -1):
        fa *= i
    return fa

def roots(a, b, c):

    delta = b**2 - 4*a*c

    if delta == 0 :
        return (-b)/(2*a)
    if delta > 0:
        return ((-b - math.sqrt(delta))/(2*a),(-b + math.sqrt(delta))/(2*a))
    if delta < 0:
        z = complex(0,1)
        delta *= -1
        return ((-b - z*math.sqrt(delta))/(2*a),(-b + z*math.sqrt(delta))/(2*a))


	

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	return itg.quad(lambda x : eval(function), lower, upper)[0]
    
    
	

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
