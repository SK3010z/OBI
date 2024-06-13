V = int(input())
A = int(input())
F = int(input())
P = int(input())

disponiveis = 0
contas = sorted([A,F,P])

for x in contas:
    if V - x < 0:
        break
    else:
        V -= x
        disponiveis += 1

print(disponiveis)