output = [None] * 1000 # fibonacci temp
count = 0
def Fibonacci (n):
    global count
    result = output[n]
    count +=1
    print('n = ' + str(n))

    if result == None:
        if n == 0:
            result = 0
        elif n == 1 or n == 2:
            result = 1
        else:
            result = Fibonacci(n - 1) + Fibonacci(n - 2)
        output[n] = result
    return result

# example
n = int(input('Please input the number of fibonacci polynomial:'))
print('Fibonacci(' + str(n) + '):' + str(Fibonacci(n)))
print('Count:' + str(count))