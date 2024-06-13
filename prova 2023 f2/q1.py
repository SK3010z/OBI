N = int(input())
C = str(input())
nn = 1
R = ""
for x in range(0, N):
    try:
        if C[x] == C[x + 1]:
            nn += 1
        else:
            R = f'{R}{nn} {C[x]} '
            nn = 1
    except:
        R = f'{R}{nn} {C[x]}'

print(R)

#aaaabbbccc