import unittest # import the unittest library, it is preinstalled with the python download since version 2.1

class TestStringMethods(unittest.TestCase): # create a class 

    def test_upper(self): # create module to test upper()
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self): # create module to test isupper()
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()