# Compress 6x6 Sparse Matrix by 3-tuple
NONEZERO = 0
temp = 1
Sparse = [
            [15,0,0,22,0,-15],
            [0,11,3,0,0,0],
            [0,0,0,-6,0,0],
            [0,0,0,0,0,0,],
            [91,0,0,0,0,0],
            [0,0,28,0,0,0,]
            ]

def compress(sparse):
    temp = 1
    Compress = [[None] * 3 for row in range(9)]
    Compress[0][0] = 6
    Compress[0][1] = 6
    Compress[0][2] = NONEZERO
    
    for i in range(6):
        for j in range(6):
            if sparse[i][j] != 0:
                Compress[temp][0] = i
                Compress[temp][1] = j
                Compress[temp][2] = sparse[i][j]
                temp = temp + 1
    return Compress
    
print('[Sparse Matrix]')
for i in range(6):
    for j in range(6):
        print('%d' %Sparse[i][j], end='\t')
        if Sparse[i][j] != 0:
            NONEZERO = NONEZERO + 1
    print()

CompressMatrix = compress(Sparse)

print('[Compress Sparse Matrix]')
for i in range(NONEZERO + 1):
    for j in range(3):
        print('%d' %CompressMatrix[i][j], end='\t')
    print()