import unittest
import vigenere
import random

class TestVigenere(unittest.TestCase):
    
    def setUp(self):
        self.key_size = 100
        self.valid_char = [chr(i) for i in range(43, 123)]
        self.not_int = ["string", 1j, 3.14]
        
    @staticmethod
    def random_text(size=20):
        text_list = [chr(random.randint(0x21, 0x7e)) for i in range(size)]
        return "".join(text_list)
        
    def test_valid_key(self):
        self.assertTrue(vigenere.valid_key(vigenere.random_key()))
        
        with self.assertRaises(TypeError):
            vigenere.valid_key(420)
            
        with self.assertRaises(Warning):
            vigenere.valid_key('foo')
            
    def test_random_key(self):
        random_key = vigenere.random_key(key_size=self.key_size)
        for char in random_key:
            self.assertIn(char, self.valid_char,
                          "Character in the key does not match key set")
        self.assertEqual(len(random_key), self.key_size, 
                         "Length of key is not equal to the arguement passed")
        
    def test_encrypt_decrypt(self):
        for _ in range(1000):
            random_key = vigenere.random_key(key_size=100)
            plain_text = self.random_text(size=1000)
            cipher = vigenere.encrypt(plain_text, random_key)
            self.assertEqual(vigenere.decrypt(cipher, random_key), plain_text,
                             "Decrypted cipher not equal to the plain-text")
        
        
if __name__ == "__main__":
    unittest.main()