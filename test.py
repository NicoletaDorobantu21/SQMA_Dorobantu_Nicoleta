import unittest

# Funcția pe care o vom testa
def add(a, b):
    return a + b

# Clasa de test
class TestCalculator(unittest.TestCase):
    
    # Test pentru funcția add
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5, "Suma ar trebui să fie 5")

if __name__ == '__main__':
    unittest.main()
