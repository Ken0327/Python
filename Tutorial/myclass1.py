'''
物件導向(Object-oriented,OO) - 繼承

繼承可以讓新類別建構在其他類別的基礎之上
我們前一個例子
class Human:
Python的類別都繼承自object
上述程式等同於
class Human(object):
舉個繼承的例子

例如
我們想產生一個女性(Woman)類別包含著人類(Human)類別的所有特性，
女性(Woman)裡面具有三個屬性－ 胸圍(bust)、腰圍(waist)、臀圍(hip)，
兩個方法－初始化(__init__)與印出三圍(printBWH)
'''

#myclass.py
class Human:
    def __init__(self,h=0,w=0):
        self.height=h
        self.weight=w
    def BMI(self):
        return self.weight / ((self.height/100)**2)

class Woman(Human):
    def __init__(self,h,w,bust=0,waist=0,hip=0):
        super().__init__(h,w)
        self.bust=bust
        self.waist=waist
        self.hip=hip
    def printBWH(self):
        print("bust={},waist={},hip={}".format(self.bust,self.waist,self.hip))


#main.py
import myclass
a = myclass.Woman(165,54,83,64,84)
print(a.BMI())
a.printBWH()

'''
super().__init__會呼叫基礎類別(Human)中的__init__
因為Woman繼承Human，所以可以使用Human中的屬性以及方法
'''