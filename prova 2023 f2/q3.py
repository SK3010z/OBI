N = int(input())
s = []

for x in range(N):
    s.append(int(input()))

m = 0

for x in range(N):
    i = set()
    for n in range(x, N):
        if s[n] not in i:
            i.add(s[n])
        else:
            m = max(m, len(i))
            break

print(m)
