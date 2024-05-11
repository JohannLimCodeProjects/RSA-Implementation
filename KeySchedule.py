import math

# Eulers Totient
def eulersTotient(p,q):
    '''
    eulersTotient:
    
    Returns the eulers totient using (p-1)(q-1)
    '''
    
    return ((p - 1) * (q - 1))


def findGCD(a,b):
    '''
    findGCD:
    
    Wrapper for math.gcd function
    Calculates the greatest common denominator of two given values
    '''
    
    return math.gcd(a,b) 

def findTheValuesOfE(eulers_totient):
    '''
    findTheValuesOfE: 
    
    Using the eulers totient calculate the values of e which result in a gcd of 1
    '''
    gcd = 0
    e = 1
    values_of_e = []
    while e != eulers_totient:
        gcd = findGCD(e,eulers_totient)
        if gcd == 1:
            values_of_e.append(e)
        else:
            pass
        e+= 1
    return values_of_e

# Function to get Euclidean Algorithm
def extended_gcd(a, b):
   """
   Extended Euclidean Algorithm to find the greatest common divisor
   and coefficients x, y such that ax + by = gcd(a, b).
   """
   if a == 0:
       return (b, 0, 1)
   else:
       g, x, y = extended_gcd(b % a, a)
       return (g, y - (b // a) * x, x)

# Function to get the modular Inverse
def modular_inverse(a, m):
   """
   Compute the modular multiplicative inverse of a modulo m.
   Raises an exception if the modular inverse does not exist.
   """
   g, x, y = extended_gcd(a, m)
   if g != 1:
       raise Exception('Modular inverse does not exist')
   else:
       return x % m

def key_schedule(p,q):
    n = p*q
    eulers = eulersTotient(p,q)
    values_of_e = findTheValuesOfE(eulers)

    print(f"Choose one of the following to use to produce the public and private keys:{values_of_e}")
    e_search = int(input())
    for e in values_of_e:
        if e == e_search:
            break
        
    d = modular_inverse(e,eulers)

    return d,n,e