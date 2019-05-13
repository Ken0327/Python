# str.format()可以非常方便的建立字串
s = "The {0} {1} tower has {1} floors above ground and five underground.".format("taipei",101)
print(s) 

# 也可以省略欄位名稱
s = "The {} {} tower has {} floors above ground and five underground.".format("taipei",101,101)
print(s)

# 欄位名稱也可以用關鍵字引數來給予
s = "The {location} {num} tower has {num} floors above ground and five underground.".format(num=101,location="taipei")
print(s)

# 群集資料型態利用索引來指定資料項
l = ["taipei","taichung","tainan",100,101,102]
s = "The {0[0]} {0[4]} tower has {0[4]} floors above ground and five underground.".format(l)
print(s)

# dict(字典)型態
d = {"city":"taipei","num":101}
s = "The {0[city]} {0[num]} tower has {0[num]} floors above ground and five underground.".format(d)
print(s)