# sympy package includes an isprime function
import sympy
import math

# Prime Test
def checkIfPrime(value):
    '''
    checkIfPrime:
    
    Wrapper for sympy.isprime
    Checks if a value is a prime number
    '''
    return sympy.isprime(value)

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


#Key Schedule

#Extended Euclidian Algorithm

# while True:
#     print("Enter a prime number for the value of p")
#     p = input()
#     if checkIfPrime(p) is True:
#         break
#     else:
#         print("Reenter a prime number p")

# while True:
#     print("Enter a prime number for the value of q")
#     q = input()
#     if checkIfPrime(q) is True:
#         break
#     else:
#         print("Reenter a prime number q")



