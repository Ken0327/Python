'''
decorator寫法
'''
def print_my_name(name):
    print "I am %s" %(name())

@print_my_name
def my_name():
    return "Hans"
#print my_name() #TypeError: 'NoneType' object is not callable
print my_name
print print_my_name

'''
decorator 就是用來解決最後這一行的問題 “my_name = print_my_name(my_name)” ，
讓 my_name 不要重覆寫兩次，就這麼簡單，嚴格來說 decorator 的作用根本稱不上”裝飾“的意思。
'''
def print_my_name(name):
    print "I am %s" %(name())

def my_name():
    return "Hans"

print my_name()
print my_name
my_name = print_my_name(my_name)
#print my_name() #TypeError: 'NoneType' object is not callable
print my_name
print print_my_name
'''
my_name = print_my_name(my_name) 這段的意思是把 my_name 這個 function 傳進 print_my_name 做處理，

然後把 print_my_name(my_name) 的回傳值重新綁定在 my_name 變數上。原本 my_name 是 function，但是因為重新綁定的關係，

my_name 已經不是一個 function，而是與 print_my_name(my_name) 的 return 值綁定在一起，由於 print_my_name 沒有特別指定 return 什麼東西，

python 就會默認 return None，所以執行 print my_name 指令就會得到 None。

也因為 my_name 已經不是 function 的關係 ，call 它的話就會得到 TypeError: ‘NoneType’ object is not callable。

如果要讓 my_name 可以被 call，只要加一行 return function 就可以了，如下例。
'''
def print_my_name(name):
    print "I am %s" %(name())
    return name # return 傳進來的 function

@print_my_name
def my_name():
    return "Hans"

print my_name()
print my_name
#print print_my_name()
print print_my_name
'''
這樣 my_name 就又可以被 call 了。

說穿了 decorator 就是個便利寫程式的語法糖。

'''