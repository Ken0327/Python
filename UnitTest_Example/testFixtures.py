import unittest

class FixturesTest(unittest.TestCase):

    def setUp(self):
        print('In setUp()')


    def tearDown(self):
        print('In tearDown()')


    def test(self):
        print('in test()')


if __name__ == '__main__':
    unittest.main()