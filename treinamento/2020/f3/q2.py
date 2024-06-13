from math import gcd
N, M = map(int, input().split())
S = list(map(int, input().split()))
x = 1
c = 0
r = []

m = [] # matriz das operações

for i in range(0, M):
    m.append(list(map(int, input().split()))) #inteiros q serão atribuída seus valores em outras variáveis depois


for i in m: #percorre a matriz
    T = i[0] #obtem o tipo de operação da vez
    if T == 1: # se a operação for do tipo 1
        #print('teste1')
        I = i[1] - 1 # indice do elemento na sequencia a ser troca (-1 para ser um índice em python)
        V = i[2] # o elemento na sequencia de indice I será trocado para V
        S[I] = V # faz a troca do elemento

    else: # se a operação for do tipo 2
        #print('teste2')
        E = i[1] - 1 #índice do elemento inicial (-1 para ser um índice em python)
        D = i[2] #índice do elemento final de um intervalo contíguo da sequência S (por ser o ultimo termo, nao -1)

        while x <= len(range(E, D)): # para quando o tamanho das subsequencias for maior que o intervalo
            #print('teste2.1')
            for i in range(E, D): #percorre os elementos, usando x para quantos elementos a frente usar
                #print('teste2.2')
                ie = S[i:i+x] #intervalo dos elementos
                #print('teste2.21 ----->', S[i:i+x], "  ", len(ie))
                #print('teste2.22 ---->', x)

                # se o mdc da lista de elementos desempacotada como argumentos for > 1
                if gcd(*S[i:i+x]) > 1 and (int(len(ie)) == x): #ao ultrapassar, ele nao da erro, mas ainda imprime o que deu
                    c += 1 # numero de candidatas += 1
                #print('teste2.3 ->', c)


            x += 1
        x = 1


        r.append(c)
    c = 0


for x in r:
    print(x)









