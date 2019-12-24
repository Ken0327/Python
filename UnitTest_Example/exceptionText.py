import unittest

# 舉例來說，如果我們預期會有除以零ZeroDivisionError的錯誤，那麼就可以利用 assertRaises來處理


def myFun(a, b):
    print(a, b)
    c = a/b


class ExceptionTest(unittest.TestCase):

    def test_assert_raises(self):
        self.assertRaises(ZeroDivisionError, myFun, 20, 0)


if __name__ == '__main__':
    unittest.main()
