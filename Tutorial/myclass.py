'''
物件導向(Object-oriented,OO) - 定義類別
例如
我們產生一個人類(Human)類別，裡面具有兩個屬性－身高(self.height)與體重(self.weight) ，兩個方法－初始化(__init__)與計算BMI(BMI)
'''
#myclass.py
class Human:
    def __init__(self,h=0,w=0):
        self.height=h
        self.weight=w
    def BMI(self):
        return self.weight / ((self.height/100)**2)



#main.py
import myclass
a = myclass.Human(180,80)
print(a.BMI())

'''
當Python建立物件時，會先呼叫__new__()建立物件，之後呼叫__init__()進行物件初始化。

由於我們並未建立__new__()方法，所以Python會去找Human基礎類別裡的__new__()，這邊會去找object.__new__()

再來會去呼叫Human.__init__()進行初始化

在Python中，方法的第一個參數是指向物件本身的參照，習慣命名用self
'''