def terribleRoot(n):
    #adds epsilon to the guess until the guess is bigger that the actual root
    epsilon = .5 ** 10
    guess = 0
    while guess ** 2 < n:
        guess += epsilon
    return (guess + (guess - epsilon)) / 2 #taking the average of the guesses that're too big and too small is my attempt at trying to get a bit better output. Its almost doing one iteration of a bisection search.
    
def bisectionRoot(n):
    #find the square root using bisection
    low = 0
    high = n
    epsilon = .5 ** 20
    while not abs(n - (low*high)) < epsilon: #do a bisection search until the output is within a tolerence of epsilon of the actual root.
        aver = (low+high)/2
        if aver**2 >= n:
            high = aver
        else:
            low = aver
    return aver

def newtonRoot(n):
    #find the square root using Newton's method
    guess1 = 1
    guess2 = n
    while not guess1 == guess2: #unlike the one using bisection, this algorithm can simply terminate when the previous two guesses are the same without adding alot of runtime like the bisection algorithm.
        guess2 = guess1
        guess1 = .5*(guess1+(n/guess1))
    return guess1

def sqrt(n):
    #if I create a new root algorithm, I can easily substitute it in here, not having the change its function name here to be less discriptive while still being able to use sqrt() in other files.
    return newtonRoot(n)