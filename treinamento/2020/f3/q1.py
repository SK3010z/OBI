from math import *
A = int(input())
B = int(input())
x = 0 # comprimento do quadrado total
y = 0 # largura do quadrado total
p = False # é POSSIVEL o quadrado com as informações dadas?

qb = int(sqrt(B))

for l in range(1, qb + 1):
    # l = largura
    c = B / l # comprimento
    if c % 1 == 0: #se for inteiro, no caso, nao faltar azulejos para completar o quadrado de respectiva largura
        c = int(c)
        qtdA = c*2 + l*2 + 4 #comprimento.2 + largura.2 + 4(quinas do quadrado de fora) = qtd de blocos A de arcordo com os blocos B

        if qtdA == A: # se a suposição estiver certa,
            x = c + 2
            y = l + 2
            p = True
            break

if p:
    if x < y:
        print(x,y)
    else:
        print(y,x)
else:
    print(-1,-1)
