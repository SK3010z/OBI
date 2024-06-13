S, T = map(int, input().split())

tuneis = []
for _ in range(T):
    X, Y = map(int, input().split())
    tuneis.append((X, Y))

P = int(input())

sugestoes = []
for _ in range(P):
    entrada = input().split()
    N = int(entrada[0])
    passeio = list(map(int, entrada[1:]))
    sugestoes.append((N, passeio))

count = 0
for N, passeio in sugestoes:
    passeio_valido = True
    for i in range(N - 1):
        if (passeio[i], passeio[i + 1]) not in tuneis and (passeio[i + 1], passeio[i]) not in tuneis:
            passeio_valido = False
            break
    if passeio_valido:
        count += 1

print(count)
