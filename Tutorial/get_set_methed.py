'''
class Person:
    
    def __init__(self):
        self._age = None

    def get_age(self):
        return self._age

    def set_age(self,age):
        if(isinstance(age,str)):
            self._age = int(age)
        elif(isinstance(age,int)):
            self._age = age

    age = property(get_age,set_age)

p = Person()
p.set_age(18)
a = p.get_age()
age = p.age
print(a)
print(age)
'''

'''
Property Metheod
'''
class Person(object):
    
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        if isinstance(age,str):
            self._age = int(age)
        elif isinstance(age,int):
            self._age = age

    @age.deleter
    def age(self):
        del self._age

'''
p = Person()
p.age = "18"
print p.age #18
del p.age
print p.age #报错,AttributeError: 'Person' object has no attribute '_age'
'''

Person.age = "18"
print Person.age #18
del Person.age
print Person.age
