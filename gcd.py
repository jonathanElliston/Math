def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a%b)
    
def lcm(a,b):
    if a < b:
        a, b = b, a
    return int(a/gcd(a,b)*b)

def addIntFractions(num1, den1, num2, den2):
    num3 = num1*den2 + num2*den1
    den3 = den1*den2
    return int(num3/(gcd(num3, den3))), int(den3/(gcd(num3, den3)))