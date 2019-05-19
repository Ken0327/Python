# Compress 2D lower triangular matrix to 1D matrix
ArraySize = 5
A = [
        [76,0,0,0,0],
        [54,51,0,0,0],
        [23,8,26,0,0],
        [43,35,28,18,0],
        [12,9,14,35,46]
    ]
# num = 1+2+3+...+n = n(n+1)/2
num = int(ArraySize*(ArraySize + 1)/2)
# declare B[]
B = [None] * num

index = 0
for i in range(ArraySize):
    for j in range(i + 1):
        if (A[i][j] != 0):
                B[index] = A[i][j]
                index += 1

print('[Lower triangular Matrix]')
for i in range(ArraySize):
	for j in range(ArraySize):
		print('%d' %A[i][j], end='\t')
	print()
print('[Compress to 1D matrix]')
print(B)