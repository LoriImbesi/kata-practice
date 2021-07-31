import unittest

from helloWorld import sayHello


class TestHelloWorld(unittest.TestCase):

    def test_sayHello(self):
        self.assertEqual("Hello World", sayHello("Hello World"))


if __name__ == '__main__':
    unittest.main()
