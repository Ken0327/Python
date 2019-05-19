# Compress 2D upper triangular matrix to 1D matrix
ArraySize = 5
A = [
        [7,8,12,21,9],
        [0,5,14,17,6],
        [0,0,7,23,24],
        [0,0,0,32,19],
        [0,0,0,0,8]
    ]
# num = 1+2+3+...+n = n(n+1)/2
num = int(ArraySize*(ArraySize + 1)/2)
# declare B[]
B = [None] * num

index = 0
for i in range(ArraySize + 1):
    for j in range(i, ArraySize):
        if (A[i][j] != 0):
                B[index] = A[i][j]
                index += 1

print('[Upper triangular Matrix]')
for i in range(ArraySize):
	for j in range(ArraySize):
		print('%d' %A[i][j], end='\t')
	print()
print('[Compress to 1D matrix]')
print(B)