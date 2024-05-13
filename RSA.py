# sympy package includes an isprime function
import gmpy2
import math
from KeySchedule import *
import os
import random

def binary_modular_exponentiation(base,exponent,modulus):
    '''
    Binary Modular Exponentiation:
    
    Binary modular exponentiation takes advantage of the binary representation of the exponent. 
    Instead of multiplying the base by itself for each bit of the exponent, it squares the base each time and performs modular reduction at each step. 
    This reduces the number of multiplications required, making the computation much faster.

    Parameters:
    base(int): Base for binary modular exponentiation
    exponent(int): The exponent to raise the base by
    modulus(int): The value of the modulus to take by

    Returns:
    result: the value of the modulus after applying the exponent
    '''

    result = 1
    base = base % modulus  # Make sure base is within range

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        #Integer division, divides lh by rh
        exponent //= 2

    return result

def checkIfPrime(p):
    '''
    Check If Prime:

    The function checks if the value is a prime number using binary modular exponentiation.

    Parameters:
    p(int): the value to test if it is a prime number or not
    
    Returns:
    1 if the value is prime
    '''

    if p == 2:
        return True
    return binary_modular_exponentiation(2, p - 1, p) == 1
    
def encrypt(message, n, e):
    '''
    Encrypt:

    Encrypts the message using the RSA algorithm and its public key

    Parameters:
    n(int): the value of p * q
    e(int): the public key
    
    Returns:
    ciphertext(str): The encrypted text
    '''

    ciphertext = ""
    n_hex_length = len(hex(n))
    for char in message:
        int_char = ord(char)
        encrypted_char = gmpy2.powmod(int_char,e,n)
        hex_char = encrypted_char.digits(16)
        hex_char = hex_char.zfill(n_hex_length)
        ciphertext += hex_char
    
    return ciphertext

def decrypt(encrypted_text, n, d):
    '''
    Decrypt:

    Decrypts the message using the RSA algorithm and its private key

    Parameters:
    n(int): the value of p * q
    d(int): the private key
    
    Returns:
    decrypted_text(str): The decrypted text
    '''
    decrypted_text = ""
    
    n_hex_length = len(hex(n))
    for i in range(0,len(encrypted_text),n_hex_length):
        hex_char = encrypted_text[i:i+n_hex_length]
        encrypted_char = gmpy2.mpz(hex_char,base =16)
        decrypted_char = gmpy2.powmod(encrypted_char,d,n)
        decrypted_char = chr(int(decrypted_char))

        decrypted_text += decrypted_char
    return decrypted_text   

def generate_random_prime():
    '''
    Generate Random Prime:

    Function which implements prime number generation which is larger than 2^64

    Using get randbits we generate a value which is at least 65 bits in length therefore larger than 2^64.

    Returns:
    candidate: a value which is prime
    '''

    while True:
        # Generate a random number with at least 128 bits
        candidate = random.getrandbits(65)
        # Ensure the number is odd to increase the chance of being prime
        # Converts the result of candidate to and odd value by changing the value of the right most bit
        candidate |= 1
        # Perform primality testing using Miller-Rabin test
        if checkIfPrime(candidate) == 1:
            return candidate

if __name__ == "__main__":

    # Generate random values of p and q which are larger than 2^64
    p = generate_random_prime()
    q = generate_random_prime()
    print(f"Generated random primes P:{p} , Q: {q}")

    cwd = os.getcwd()
    dirFiles = os.listdir(cwd)
    for file in dirFiles:
        if file.endswith(".txt"):
            print(file)
    # While loop to determine the input text file
    while True:
        print("Select a text file from the above selection of files to encrypt:")
        fileName = input()
        filePath = os.path.join(cwd,fileName)
        if os.path.exists(filePath):
            f = open(filePath)
            message = f.read()
            break
        else:
            print("The file you wish to encrypt does not exist or is not a text file")

    print("Generating Keys....")
    d,n,e = key_schedule(p,q)
    print(f"d:{d} n: {n} e: {e}")
    #Output the encrypted and decrypted text files
    #Encryption code
    print("Encrypting....")
    encrypted_text = encrypt(message,n,e)
    savePath = "./out/Encrypted.txt"
    with open(savePath,"w") as e:
        e.write(str(encrypted_text))
    print(f"Encrypted file saved to {savePath}")
    outPath = os.path.join(cwd,"out")
    outPathFiles = os.listdir(outPath)

    #Decryption code
    print(f"Choose a file to decrypt from {outPathFiles}")
    fileName = input()
    decryptPath = os.path.join(outPath,fileName)
    with open(decryptPath,"r") as r:
        text_in_file = r.read()
    decrypted_text = decrypt(text_in_file,n,d)
    print(f"Decrypted Text: {decrypted_text}")
    with open("./out/Decrypted.txt","w") as d:
        d.write(decrypted_text)