V = -1
A = -1
F = -1
P = -1

while not (0 <= V <= 2000 and 1 <= A <= 1000 and 1 <= F <= 1000 and 1 <= P <= 1000):
    if not (0 <= V <= 2000):
        V = int(input())
    if not (1 <= A <= 1000):
        A = int(input())
    if not (1 <= F <= 1000):
        F = int(input())
    if not (1 <= P <= 1000):
        P = int(input())

contas = [A, F, P]
contas.sort()
c = 0

if V >= contas[0]:
    c += 1
    V -= contas[0]

if V >= contas[1]:
    c += 1
    V -= contas[1]

if V >= contas[2]:
    c += 1

print(c)