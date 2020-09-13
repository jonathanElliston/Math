from gcd import *
from primeTest import *
from random import *
from functools import *
    
def pollardP(n):
    #pollardP is factoring algorithm which finds a prime factor of n
    
    #print("pollardP", n)
    # ^ is debugging for when this is used in other functions
    
    if isPrime(n): #pollardP will not terminate if given a prime
        print("Prime was passed into pollardP")
        return
    
    #generate a random polynomial equation
    #I use a quadratic with coefficients ∈ [-10, 10]
    a = randrange(-10, 10)
    b = randrange(-10, 10)
    c = randrange(-10, 10)
    def f(x):
        return a*x*x + b*x + c
    
    #set up vars for loop
    x = 2
    y = 2
    d = 1    
    
    while True:
        #print(x, y, a, b, c, d) #debugging
        
        #set x to be f(x), y to be f^2(y), and d to be the gcd of (the difference between x and y) and (n)
        #(this is all done modulo n)
        #this means that eventually the difference between x and y shares a common factor n, and if so, we factored n

        x = f(x)
        y = f(f(y))
        d = gcd(abs(x-y), n)
        
        if d == n: #if d = n, then we need to restart the algorithm
            a = randrange(-10, 10)
            b = randrange(-10, 10)
            c = randrange(-10, 10)
            def f(x):
                return a*x*x + b*x + c
            x = 2
            y = 2
        
        x = x%n
        y = y%n
        
        
        if d == n: #if d = n, then we need to restart the algorithm
            a = randrange(-10, 10)
            b = randrange(-10, 10)
            c = randrange(-10, 10)
            def f(x):
                return a*x*x + b*x + c
            x = 2
            y = 2
        
        elif d != 1: #if d is not 1 or n, then we factored n
            
            
            if d * int(n/d) == n: #I was having some wierd bugs with it not factoring correctly, this is my bad fix before I can debug better
                return d, int(n/d)
            else:
                return pollardP(n)


def badFactor(n):
	if isPrime(n):
		print("Prime was passed into pollardP")
		return
	
	for i in range(int(sqrt(n)) + 1):
		if n/i == n//i:
			return i
	
            
                
                
                

def factorPrimitive(n):
	return badFactor(n)


#factor4 will be remembering which numbers are prime
#use appending to an output to do this
def factor(n):
    output = []
    listn = [n]
    while listn:
        val = listn[0]
        del listn[0]
        if isPrime(val):
            output.append(val)
        else:
            a, b = pollardP(val)
            #print(val)
            assert a * b == val
            listn.append(a)
            listn.append(b)
    
    assert reduce(lambda a, b: a*b, output) == n
    
    return sorted(output)