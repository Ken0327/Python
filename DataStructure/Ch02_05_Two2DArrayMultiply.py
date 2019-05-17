# 示範兩個矩陣相乘

def MatrixMultply(arrA, arrB, arrC, M, N, P):
    global C
    if M <=0 or N <=0 or P <=0:
        print('[Error: dimension M N P must > 0]')
        return
    for i in range(M):
        for j in range(P):
            Temp = 0
            for k in range(N):
                Temp = Temp + int(arrA[i * N + k]) * int(arrB[k * P + j])
            arrC[i * P + j] = Temp

print('Please input dimension of Matrix A (M,N):')
M = int(input('M = '))
N = int(input('N = '))
A = [None] * M * N

print('[Please input value of Matrix A]')
for i in range(M):
    for j in range(N):
        A[i*N+j] = input('a%d%d=' %(i,j))

print('Please input dimension of Matrix B (N,P):')
N = int(input('N = '))
P = int(input('P = '))
B = [None] * N * P

print('[Please input value of Matrix B]')
for i in range(N):
    for j in range(P):
        B[i*P+j] = input('b%d%d=' %(i,j))

C = [None] * M * P
MatrixMultply(A, B, C, M, N ,P)
print('[A x B = ]')
for i in range(M):
    for j in range(P):
        print('%d' %C[i*P+j], end='\t')
    print()