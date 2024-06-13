N = int(input())
nomes = []
lances = []
ganhador = ''
maiorlance = 0

for x in range(0, N):
    C = str(input())
    V = int(input())
    nomes.append(C)
    lances.append(V)

for n, x in enumerate(lances):
    if x > maiorlance:
        ganhador = nomes[n]
        maiorlance = x


print(ganhador)
print(maiorlance)
