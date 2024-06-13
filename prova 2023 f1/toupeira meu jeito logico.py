S, T = map(int, input().split())
caminhos = {}
rf = 0 #resultado final
for i in range(0, T): #definição dos caminhos possiveis
    X, Y = map(int, input().split())

    if str(X) not in caminhos:  # se nao existir a chave ainda, cria ela
        caminhos[str(X)] = []
    caminhos[str(X)].append(Y)

    if str(Y) not in caminhos: # se nao existir a chave ainda, cria ela
        caminhos[str(Y)] = []
    caminhos[str(Y)].append(X)

P = int(input())

for i in range(0, P):
    p = list(map(int, input().split()))
    N = p[0] # quantos movimentos
    na = p[1] #casa atual
    C = p[2:N+1] #caminho
    r = 0

    for x in range(0, len(C)):
        if int(C[x]) in caminhos[str(na)]: #se o proximo caminho estiver nas rotas do caminho atual
            r = 1 # permanece no 1, no caso possivel até que aja alguma falha na rota
        else:
            r = 0 #assim que der a primeira falha na rota
            break
        na = C[x]
    rf += r  # rf + 1 no caso de ser possivel, r + 0 caso nao seja possivel

print(rf)

