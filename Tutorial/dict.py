'''
dict是屬於無序的映射(mapping)型態

映射是由key:value所構成的群集

key必須為不可變的資料型態(int、float、str....)

建立dict的方法如下
'''
dict_1 = dict({"a":1111,"b":2222,"c":3333})
dict_2 = dict(a=1111,b=2222,c=3333)
dict_3 = {"a":1111,"b":2222,"c":3333}

'''
字典的key必須是唯一的
要取出裡面的value使用 中括號
'''
dict_1["a"]
dict_2["b"]
dict_3["c"]

#新增
dict_1["d"]=4444
#刪除
del dict_1["d"]

#範例
dict_1 = dict({"a":1111,"b":2222,"c":3333})
dict_2 = dict(a=1111,b=2222,c=3333)
dict_3 = {"a":1111,"b":2222,"c":3333}
print(dict_1["a"])
print(dict_2["b"])
print(dict_3["c"])

dict_1["d"]=4444
print(dict_1)
del dict_1["d"]
print(dict_1)


'''
當一個dict，我們想取出他的key,value資料項，可以使用下列方法進行迭代走訪dict.items()
'''
print('dict_1.items()')
dict_1 = dict({"a":1111,"b":2222,"c":3333})
for i in dict_1.items():
    print(i[0],i[1])

dict_1 = dict({"a":1111,"b":2222,"c":3333})
for k,v in dict_1.items():
    print(k,v)

'''
若只迭代dict的value，可使用dict.values()
'''
print('dict_1.values()')
dict_1 = dict({"a":1111,"b":2222,"c":3333})
for v in dict_1.values():
    print(v)

'''
若要迭代dict的key，可使用dict.keys()或者直接迭代dict
'''
print('dict_1.keys()')
dict_1 = dict({"a":1111,"b":2222,"c":3333})
for k in dict_1:
    print(k)
for k in dict_1.keys():
    print(k)

'''
dict.items()、dict.keys()、dict.values()會傳回dictionary view，dictionary view是一個可迭代的物件

'''
