# Python 可以藉由 raise 引發例外
try:
    raise OverflowError
except OverflowError:
    print("產生OverflowError例外")


# 自定義的例外
class InputError(Exception):
    pass


a= input("輸入1~100數字:")
a= int(a)
try:
    if a<=0 or a>=100:
        raise InputError
except  InputError:
    print("輸入錯誤")
else:
    print(a)