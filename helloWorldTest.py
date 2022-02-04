import unittest

from helloWorld import sayHello, multiplyTwoNumbers, oddOrEven


class TestHelloWorld(unittest.TestCase):

    def test_sayHello(self):
        self.assertEqual("Hello World", sayHello("Hello World"))

    def test_multiplyTwoNumbers(self):
        self.assertEqual(12, multiplyTwoNumbers(3, 4))

    def test_oddOrEven(self):
        self.assertEqual("even", oddOrEven(10))
        self.assertEqual("odd", oddOrEven(7))
        self.assertEqual("0", oddOrEven(0))
        self.assertEqual("odd", oddOrEven(-5))
        self.assertEqual("even", oddOrEven(-4))
        
    
    


if __name__ == '__main__':
    unittest.main()
