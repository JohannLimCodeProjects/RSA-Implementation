import math
import time

# Eulers Totient
def eulersTotient(p,q):
    '''
    eulersTotient:
    
    Parameters:
    p(int): prime number p
    q(int): prime number q

    Returns the eulers totient using (p-1)(q-1)
    '''
    
    return (p - 1) * (q - 1)


def findGCD(a,b):
    '''
    findGCD:
    
    Parameters:
    a(int): first value of gcd
    b(int): second value of gcd

    Wrapper for math.gcd function
    Calculates the greatest common denominator of two given values
    '''
    
    return math.gcd(a,b) 

def findTheValuesOfE(eulers_totient):
    '''
    findTheValuesOfE: 
    
    Parameters:
    eulers_totient(int): the value of eulers totient calculated using the above method

    Using the eulers totient calculate the values of e which result in a gcd of 1
    '''
    gcd = 0
    e = 0
    values_of_e = []
    while e != eulers_totient:
        print(e)
        gcd = findGCD(e,eulers_totient)
        # print(e,gcd,eulers_totient)
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

    Parameters:
    a(int): first value of gcd
    b(int): second value of gcd

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

    Parameters:
    a(int): the value you wish to calculate the mod off
    m(int): the mod value

    """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def key_schedule(p,q):
    """
    Key schedule algorithm to generate both keys using the above .
    Raises an exception if the modular inverse does not exist.

    Parameters:
    p(int): prime number p
    q(int): prime number q

    Returns:
    d(int): private key
    n(int): value of p * q
    e(int): public key

    """

    n = p*q
    eulers = eulersTotient(p,q)
    # print(eulers)
    # values_of_e = findTheValuesOfE(eulers)

    # e_search = 65537
    e = 65537
    # # for e in values_of_e:
    #     print(e)
    #     if e == e_search:
    #         print("Found 65537")
    #         break
    
    d = modular_inverse(e,eulers)

    return d,n,e
