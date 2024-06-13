from math import fsum
L, C = map(int, input().split())
P = int(input())
m = []
r = 0 #resultado final




for x in range(0, L):
    m.append([]) #coloca uma nova linha
    for i in range(0, C):
        m[x].append(0)


def verify(x, y):
    rr = []
    try:
        rr.append(m[x-1][y])
    except:
        rr.append(-1)
    try:
        rr.append(m[x][y-1])
    except:
        rr.append(-1)
    try:
        rr.append(m[x+1][y])
    except:
        rr.append(-1)
    try:
        rr.append(m[x][y+1])
    except:
        rr.append(-1)

    rr.append(str(x))
    rr.append(str(y))

    return rr
#atraves do indice que as direções (cima, baixo, esquerda, direita) com a função verify retorna
def set(x, y, t): #exclui os quadrados brancos nao favoraveis

    if t == 0:
        m[x - 1][y] = 0
        m[x][y] = 2
    elif t == 1:
        m[x][y - 1] = 0
        m[x][y] = 2
    elif t == 2:
        m[x + 1][y] = 0
        m[x][y] = 2
    elif t == 3:
        m[x][y + 1] = 0
        m[x][y] = 2



# v[0] cima
# v[1] esquerda
# v[2] baixo
# v[3] direita





for i in range(0, P):
    X, Y = map(int, input().split()) # onde colocar a peça preta
    X -= 1 #coverter para índice python
    Y -= 1 #coverter para índice python
    m[X][Y] = 1 # coloca as peças pretas na matriz
    v = verify(X, Y) #valores das casas retas adjacentes
    b = 0 # brancas colocáveis
    print(v)

    if v[0] == 0 and X != 0:
        cima = verify(X - 1, Y)
        x, y = int(cima[4]), int(cima[5]) # obtem as coordenadas da parte de cima
        if cima.count(2) == 0: #se nao tiver nenhuma perto, coloca

            m[X - 1][Y] = 2
        elif cima.count(2) == 1:
            ind = cima.index(2)
            set(x,y, ind)



    if v[1] == 0 and Y != 0:
        esquerda = verify(X, Y - 1)
        x, y = int(esquerda[4]), int(esquerda[5])
        if esquerda.count(2) == 0: #se nao tiver nenhuma perto, coloca
            m[X][Y - 1] = 2

        elif esquerda.count(2) == 1:
            ind = esquerda.index(2)
            set(x,y, ind)


    if v[2] == 0 and X != L-1: # -1 pq ainda nao tinha sido convertida para indice python
        baixo = verify(X + 1, Y)
        x, y = int(baixo[4]), int(baixo[5])
        if baixo.count(2) == 0: #se nao tiver nenhuma perto, coloca
            m[X + 1][Y] = 2

        elif baixo.count(2) == 1:
            ind = baixo.index(2)
            set(x,y, ind)

    if v[3] == 0 and X != C-1: # -1 pq ainda nao tinha sido convertida para indice python
        direita = verify(X, Y + 1)
        x, y = int(direita[4]), int(direita[5])
        if direita.count(2) == 0: #se nao tiver nenhuma perto, coloca
            m[X][Y + 1] = 2

        elif direita.count(2) == 1:
            ind = direita.index(2)
            set(x,y, ind)


    for x in m:
        print(x)

for x in m:
    r += x.count(2)

print(r)

