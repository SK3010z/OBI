#E e R representando respectivamente o número de estações e o número de ramos de trilhos da rede ferroviária da mina
E, R = map(int, input().split())
e = range(1, E+1)

ABC = []
#A e B representam as estações ligadas pelo ramo de trilho, e C representa o comprimento do ramo de trilho
# 1 2 10
# 1 3 12
# 3 4 7
# 1 4 6


for i in range(0, R):
    A, B, C = map(int, input().split())
    ABC.append([A,B,C])

K = int(input())
#X e T, que indicam respectivamente a estação pela qual Herculano quer que o trem entre e o comprimento do trem.
XT = []

# 2 18
# 1 10
# 4 26
# 3 25

for i in range(0, K):
    X, T = map(int, input().split())
    XT.append([X,T])


for x in XT:
    X = x[0]
    T = x[1]

#nao da

