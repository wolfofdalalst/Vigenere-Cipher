import unittest
import vigenere

class TestRandom(unittest.TestCase):
    
    def setUp(self):
        self.not_int = ["string", 1j, 3.14]
    
    def test_randint(self):
        self.assertTrue(10 <= vigenere.randint(10, 1000) <= 1000,
                        "Randint is not within the interval provided")
        with self.assertRaises(TypeError):
            vigenere.randint(i for i in self.not_int)
            
if __name__ == "__main__":
    unittest.main()