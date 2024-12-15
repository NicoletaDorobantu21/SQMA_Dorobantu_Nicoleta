import unittest

# Funcția care verifică dacă un număr este par
def is_even(number):
    return number % 2 == 0

# Clasa de test
class TestEvenOdd(unittest.TestCase):
    
    # Test pentru funcția is_even
    def test_is_even(self):
        self.assertTrue(is_even(4), "4 ar trebui să fie un număr par")
        self.assertFalse(is_even(5), "5 ar trebui să fie un număr impar")

if __name__ == '__main__':
    unittest.main()
