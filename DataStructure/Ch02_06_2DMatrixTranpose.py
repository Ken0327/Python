arrA = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16,]]
N = 4
# Declare 4x4 Matrix arr
arrB = [[None] * N for row in range(N)]

print('[Original Matrix]')
for i in range(4):
    for j in range(4):
        print('%d' %arrA[i][j], end='\t')
    print()

# Transpose matrix
for i in range(4):
    for j in range(4):
        arrB[j][i] = arrA[i][j]

print('[Transpose matrix]')
for i in range(4):
    for j in range(4):
        print('%d' %arrB[i][j], end='\t')
    print()