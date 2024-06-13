from math import sqrt, cbrt
A = int(input())
B = int(input())
r = 0

for x in range (A, B+1):
    q = sqrt(x)
    c = cbrt(x)

    if q % 1 == 0 and c % 1 == 0:
        r += 1

print(r)