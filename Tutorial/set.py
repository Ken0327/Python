'''
Python內建兩種集合型態：

可變的set與不可變的frozenset

使用{}建立set並以逗號(,)間隔

集合是無序且元素不重複
'''

a={1,2,3,3,4,5,6}
print(type(a))
print(a)
b=frozenset({2,4,6})
print(type(b))
print(b)

'''
集合內只能擺放不可變的資料型態(float、int、str、tuple....)
a={1,[5,6],3,4,5,6}
'''

'''
集合可以使用一些運算符進行操作：
|(聯集)、&(交集)、-(差集)、^(對稱差集)、<=(是否為子集合)、<(是否為真子集)、>=(是否為母集合)、>(是否為真母集)
'''
a=set("taipei")    #等同於{"t","a","i","p","e","i"}
print(a)
b={"p","e","i"}    #等同於{"p","e","i"}
print(b)
print(a|b)
print(a&b)
print(a-b)
print(a^b)
print(a<=b)
print(a<b)
print(a>=b)
print(a>b)

'''
使用方法對set進行操作：

set.add(x) - 將x加入set中

set.copy() - 傳回set的副本

set.clear() - 清除set所有資料

set.discard(x) - 移除set中的x，若找不到 "不" 引發KeyError例外

set.remove(x) - 移除set中的x，若找不到引發KeyError例外

set.pop() - 隨機傳回並移除一個資料項，set為空集合時引發KeyError例外

'''
a={1,2,3,4}
print(a)
a.add(7)
print(a)
b = a.copy()  #不可寫成b=a , python 會將b參照到同一個物件,而不是複製一份
print(b)
b.clear()
print(b)
a.discard(1)
print(a)
a.remove(2)
print(a)
k=a.pop()
print(k)
print(a)
