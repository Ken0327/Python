import unittest

class SimplisticTest(unittest.TestCase):

    def test(self):
        self.assertTrue("hello"=="hello")
if __name__ == '__main__':
    unittest.main()