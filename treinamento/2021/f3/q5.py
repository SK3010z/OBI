from math import sqrt
A = int(input())
B = int(input())
x = 0
y = 0
qB = int(sqrt(B))

for i in range(1, qB+1):

    if B % i == 0:
        cB = B / i
        lB = i
        qtdA = cB*2 + lB*2 + 4

        if qtdA == A:
            x = int(cB + 2)
            y = int(lB + 2)
            break

if x == 0 and y == 0:
    print(-1, -1)

elif x < y:
    print(f'{x} {y}')

else:
    print(f'{y} {x}')

