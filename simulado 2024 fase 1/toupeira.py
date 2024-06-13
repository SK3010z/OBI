S, T = map(int, input().split()) # S -> salas, T -> tuneis

caminhos = [set() for i in range(S+1)] #lista vazia dos caminhos de cada sala

for x in range(T): #adiciona os caminhos em cada sala
    X, Y = map(int, input().split())
    caminhos[X].add(Y) #na sala X, adiciona o caminho para a sala Y
    caminhos[Y].add(X) #na sala Y, adiciona o caminho para a sala X

P = int(input()) # P -> quantidade de sugestões
possiveis = 0 # quantidade de sugestões possiveis
for x in range(P): # faz P repetições
    sugestao = list(map(int, input().split())) # numero de salas + sugestão de caminho
    N = sugestao[0] # N -> numero de salas da sugestão
    del(sugestao[0]) # deleta o N pra nao atrapalhar, sobrando apenas a sugestão do caminho

    atual_possivel = 1 # predefine que a sugestão é possivel, pra caso nao for, desconsiderar igualando a 0
    for i in range(N-1): # N-1 pois é a quantidade de verificações ENTRE as salas
        sala_atual = sugestao[i]
        proxima_sala = sugestao[i+1]
        if proxima_sala not in caminhos[sala_atual]: #sala atual caso nao exista caminho para a proxima sala
            atual_possivel = 0 #desconsidera a sugestao atual
            break # interrompe o for loop
    possiveis += atual_possivel # se a sugestão atual é possivel adiciona 1, senão adiciona 0(msm q nada)

print(possiveis) # mostra o resultado

