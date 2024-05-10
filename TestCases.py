from RSA import *
import unittest

class TestCases(unittest.TestCase):
    
    # Test case to check if the function correctly identifies a prime number
    def test_prime_number(self):
        self.assertEqual(checkIfPrime(2), True)
        
    # Test case to check if the function correctly identifies a non-prime number
    def test_nonprime_number(self):
        self.assertEqual(checkIfPrime(10), False)
        
    # Test case to check the behavior of eulersTotient function
    def test_eulers_totient(self):
        # Test with prime numbers (5, 10)
        self.assertEqual(eulersTotient(5, 10), 36)

    # Test case to verify the behavior of findGCD function
    def test_find_gcd(self):
        # Test with large numbers
        self.assertEqual(findGCD(10, 10000), 10)

    # Test case to validate the behavior of findTheValuesOfE function
    def test_find_values_of_e(self):
        # Test with a given input (10)
        self.assertEqual(findTheValuesOfE(10), [1, 3, 7, 9])


if __name__ == "__main__":
    unittest.main()
    
