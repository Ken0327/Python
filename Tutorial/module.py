# 模組就是引入(使用)別的.py檔案
import sys
print(type(sys))
print(sys.argv)
print(sys.argv[1])


import sys as k
print(type(k))
print(k.argv)
print(k.argv[1])

from sys import argv
print(argv)
print(argv[1])


from sys import *
print(argv)
print(argv[1])
print(path)