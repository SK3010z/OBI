E, M, D = map(int, input().split())
lm = []
ld = []
le = []
rv = 0.0


for x in range(0, M):
    lm.append(input().split())
for x in range(0, D):
    ld.append(input().split())
for x in range(0, int(E/3)):
    le.append(input().split())


for x in le:
    for i in lm:
        if (i[0] in x and i[1] not in x) or (i[0] not in x and i[1] in x):
            rv += 0.5
    for i in ld:
        if (i[0] in x and i[1] in x):
            rv += 1

print(int(rv))
