N, F = map(int, input().split())
matriz = []
for x in range(N):
    terreno = str(input())
    linha = ""
    for i in terreno:

        if int(i) <= F:
            linha = linha + "*"
        else:
            linha = linha + i
    matriz.append(linha)

for a in matriz:
    print(a)
