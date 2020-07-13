def piByArctan(): #calculates pi by finding the arctangent of 1
    guess = 0 #the ouput of each iteration of the algorithm
    previousGuess = 5 #this is for a comparrison between two iterations, allowing the use of epsilon
    epsilon = .5 ** 25 #the tolerance for the precision
    counter = 0
    while abs(guess-previousGuess) > epsilon: #if the current and previous guess are sufficiently close, then a estimation is returned
        #I do two iterations of the algorithm in each loop
        counter += 1
        guess += 1/(counter*2-1)
        previousGuess = guess
        counter += 1
        guess -= 1/(counter*2-1)
    return (guess+previousGuess)*2 #return the average between the current guess and previous guess times 4


def pi(): #this is so substituting in a new algorithm for calculating pi is easy
    return piByArctan()