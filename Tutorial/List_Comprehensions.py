# 想產生一個List，儲存1*1 1*2 1*3...1*9 2*1 2*2... 9*9 所有數值
m=[]
for x in range(1,10):
    for y in range(1,10):
        m.append(x*y)
print(m)

# List Comprehensions 可以單行解決
m=[x*y for x in range(1,10) for y in range(1,10)]
print(m)


# 1 ~ 100 排除2, 3, 5的倍數
m=[]
for x in range(1,101):
    if x%2!=0 and x%3!=0 and x%5!=0:
        m.append(x)
print(m)

# List Comprehensions
m = [x for x in range(1,101) if x%2!=0 and x%3!=0 and x%5!=0]
print(m)