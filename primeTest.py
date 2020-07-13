from roots import *

def badIsPrime(n): #the naive algorithm for a primality test: checking all even numbers < sqrt(n)
    if n == 0 or n == 1: # 0 and 1 are neither prime nor composite, so I just print that they were passed in
        print("passed 0 or 1 into primality test")
        return
    for i in range(2, int(sqrt(n)) + 1, 2):
        if n%i == 0:
            return False
    return True

def isPrime(n): #I do this so if I add a better primality test, its easy to substitute it in here, not making me resort to non-discriptive names or changing all instances of the previous primality test
    return badIsPrime(n)


def allElementsArePrime(listinput): #I had a use for checking if all elements were prime in a list when I was trying to get a list of prime factors, so I made this
        allelementsprime = True
        for element in listinput:
            if not isPrime(element):
                allelementsprime = False
        return allelementsprime
    

#I've had trouble with primality tests not working for some inputs, so I made these two tests to check if the fuction is working
#these won't work now because I only have one primality test and I amn't able to check a output against something other that itself

def doesFunctionWorkRange(function): #checks if all is well for [0, 100], printing a list for which numbers failed. Very useful for see the patter in bugs
    failedNumbers = []
    for i in range(100):
        if function(i) != isPrime(i): #ol' trusty vs the scary newcomer
            failedNumbers.append(i)
    if failedNumbers:
        print("failed for", failedNumbers)
    else:
        print("function workes for range(0, 100)")

def doesFunctionWorkAll(function): #this prints all numbers that failed until I stop it. This is for checking if some high number failed for some reason. I use this after the other debugging function succeeded; otherwise the printout would be impossible to follow
    counter = 0
    while True:
        counter +=1
        if isPrime(counter) != function(counter): #proven but slower vs risky but faster
            print(counter)