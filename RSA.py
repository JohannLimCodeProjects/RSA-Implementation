# sympy package includes an isprime function
import sympy
import math
from KeySchedule import *
import os

def binary_modular_exponentiation(base,exponent,modulus):
    result = 1
    base = base % modulus  # Make sure base is within range

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2

    return result

def checkIfPrime(p):
    if p == 2:
        return True
    return binary_modular_exponentiation(2, p - 1, p) == 1

# def encrypt(ascii, n, e):
#     blocklen = len(str(n))
#     blockscalculated = ""
#     encryptedtext = ""
#     encryptedblocks = ""

#     i = 0
#     while i < len(str(ascii)):
#         encrypt_block = ascii[i:i + blocklen]
#         if int(encrypt_block) < n:
#             blockscalculated += f"|{encrypt_block}|"
#         else:
#             encrypt_block = ascii[i:i + (blocklen - 1)]
#             blockscalculated += f"|{encrypt_block}|"
#             i -= 1
            
#         encrypted = str((int(encrypt_block) ** e) % n)
#         encrypted = encrypted.zfill(4)
#         encryptedtext += encrypted
#         encryptedblocks += f"|{encrypted}|"
#         i += blocklen

#     print(blockscalculated)
#     print(encryptedblocks)
#     return encryptedtext

# def decrypt(encrypted_text, n, d):
#     blocklen = len(str(n))
#     blockscalculated = ""
#     decrypted_text = ""
#     decrypted_blocks = ""
    
#     i = 0
#     while i < len(str(encrypted_text)):
#         decrypt_block = encrypted_text[i:i + blocklen]
#         if int(decrypt_block) < n:
#             blockscalculated += f"|{decrypt_block}|"
#         else:
#             decrypt_block = encrypted_text[i:i + (blocklen - 1)]
#             blockscalculated += f"|{decrypt_block}|"
#             i -= 1
            
#         decrypted = str((int(decrypt_block) ** d) % n)
#         decrypted_text += decrypted
#         decrypted_blocks += f"|{decrypted}|"
#         i += blocklen

#     print(blockscalculated)
#     print(decrypted_blocks)
#     return decrypted_text

def encrypt(plaintext,n,e):
    # Unpack the key into it's components
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow(ord(char), e, n) for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(ciphertext,n,d):
    # Unpack the key into its components
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    aux = [str(pow(char, d, n)) for char in ciphertext]
    # Return the array of bytes as a string
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)


def encodeASCII(message):
    ASCIIstring = ""
    
    for char in message:
        ASCIIstring += str(ord(char))

    return ASCIIstring        

if __name__ == "__main__":
    cwd = os.getcwd()
    dirFiles = os.listdir(cwd)
    for file in dirFiles:
        if file.endswith(".txt"):
            print(file)
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
    
    while True:
        print("Enter a prime number for the value of p")
        p = int(input())
        # print(checkIfPrime(int(p)))
        if checkIfPrime(p) is True:
            break
        else:
            print("Reenter a prime number p")

    while True:
        print("Enter a prime number for the value of q")
        q = int(input())
        # print(checkIfPrime(q))
        if checkIfPrime(q) is True:
            break
        else:
            print("Reenter a prime number q")
    
    d,n,e = key_schedule(p,q)

    encrypted_text = encrypt(message,n,e)
    print(f"Encrypted Text: {encrypted_text}")
    
    decrypted_text = decrypt(encrypted_text,n,d)
    print(f"Decrypted Text: {decrypted_text}")