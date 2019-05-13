#for.py
ans=0
for i in range(1,16,2):
	ans+=i
print(ans)

#def.py
def  max(*a):
	num=0
	for n in a:
		if(n>num):
			num=n
	return num

print(max(10,20,11,21,50,40,100,30))