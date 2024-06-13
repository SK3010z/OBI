M, N = input().split()
M = int(M)
N = int(N)

roupas = []
for m in range(0, M):
    roupas.append(input().split())

P = int(input())
vendas = 0
for x in range(0, P):
    I, J = input().split()
    I = int(I) - 1
    J = int(J) - 1
    if int(roupas[I][J]):
        vendas += 1
        roupas[I][J] = str(int(roupas[I][J]) - 1)

print(vendas)
