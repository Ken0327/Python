count = 0
def Fibonacci (n):
    result = 0
    global count
    count +=1
    print('n = ' + str(n))   
    if n == 0:
        result = 0
        return result
    elif n == 1 or n == 2:
        result = 1
        return result
    else:
        result =  Fibonacci(n - 1) + Fibonacci(n - 2)
        return result

# example
n = int(input('Please input the number of fibonacci polynomial:'))
# for i in range(n + 1):
#     print('Fibonacci(%d)=%d' %(i, Fibonacci(i)))
print('Fibonacci(' + str(n) + '):' + str(Fibonacci(n)))
print('Count:' + str(count))