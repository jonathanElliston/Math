from gcd import *
from primeTest import *
from random import *
    
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

        x = f(x)%n
        y = f(f(y))%n
        d = gcd(abs(x-y), n)
        
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

""" 

       
def factor(n, factorlist = []):
    factorlist = factorlist.append(n)
    temp = []
    for item in factorlist:
        if isPrime(item):
            temp = temp + [item]
        else:
            temp = temp + [pollardP(item)]
            temp = temp + [int(item/pollardP(item))]
    return temp



def factor2(listn):
    if type(listn) == int:
        listn = [listn]
    listnclone = listn[:]
    for i in range(len(listnclone)):
        if not isPrime(listnclone[i]):
            print(i, listnclone)
            a, b = pollardP(listnclone[i])
            listnclone.append(a)
            listnclone.append(b)
            del listnclone[i]
            return factor2(listnclone)
            break
    return listnclone



def factor3(listn):
    if type(listn) == int:
        listn = [listn]
    
    while not allElementsArePrime(listn):
       
        for i in range(len(listn)):
           if not isPrime(listn[i]):
               a, b = pollardP(listn[i])
               listn.append(a)
               listn.append(b)
               del listn[i]
               break
    listn.sort()
    return listn

"""

#factor4 will be remembering which numbers are prime
    #use appending to an output to do this
def factor4(n):
    output = []
    listn = [n]
    while listn:
        val = listn[0]
        del listn[0]
        if isPrime(val):
            output.append(val)
        else:
            a, b = pollardP(val)
            print(val)
            assert a * b == val
            listn.append(a)
            listn.append(b)
    
    assert reduce(lambda a, b: a*b, output) == n #uses some library
    
    return sorted(output)
    
        
        
        
        
        
        
        
    return listn