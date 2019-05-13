# 想產生一個 1~100的集合，排除2的倍數、3的倍數、5的倍數

m=[]
for x in range(1,101):
    if x%2!=0 and x%3!=0 and x%5!=0:
        m.append(x)
print(m)

# List Comprehensions
n = [x for x in range(1,101) if x%2!=0 and x%3!=0 and x%5!=0]
print(n)

# Dictionary Comprehensions
set_e = {x for x in range(1,101)if x%2!=0 and x%3!=0 and x%5!=0}
print(set_e)