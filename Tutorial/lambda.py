# Python使用lambda關鍵字可以建立匿名函式
# lambda 參數1,參數2.... : 運算式
# 參數可有可無

a = lambda x: x*x
print(a(3))
a = lambda x: x*x*x
print(a(3))
a = lambda s: "hello "+s
print(a("syu"))

# 多參數使用
a = lambda x,y,z: (x+y+z)/2
print(a(3,7,5))
a = lambda s,u,d: "hello "+s+",ans="+str(u+d)
print(a("syu",7,3))