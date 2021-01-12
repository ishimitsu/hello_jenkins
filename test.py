import unittest
from hello import hello_jenkins

# python  -m unittest test_hello.Test_Hello -v

class Test_Hello(unittest.TestCase):

    def test_hello(self):
        self.assertTrue( hello_jenkins() )

if __name__ == "__main__":
    unittest.main()        
        
