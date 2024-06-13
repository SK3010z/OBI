N = int(input())
S = list()
r = 0

for x in range(0, N):
    S.append(str(input()))

for x in S:
    for n in S:
        if x in n:
            r += 1
    r -= 1

print(r)


