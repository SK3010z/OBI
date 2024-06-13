A = str(input())
B = str(input()) # deixa em str pra inserir o 0 antes
la = []
lb = []
resultA = 0
resultB = 0

if len(A) > len(B):
    for x in range(0, (len(A) - len(B))):
        B = "0" + B
elif len(B) > len(A):
    for x in range(0, (len(B) - len(A))):
        A = "0" + A

for n, x in enumerate(A):
    if int(x) > int(B[n]): # compara os numeros em respectivas posições
        la.append(int(A[n])) # numero "vencedor"

    elif int(x) == int(B[n]): #se for igual
        la.append(x)
        lb.append(x)
    else:
        lb.append(int(B[n]))

if len(la) > 0:
    for i in la:
        resultA *= 10
        resultA += int(i)
if len(lb) > 0:
    for i in lb:
        resultB *= 10
        resultB += int(i)

if int(resultA) == 0:
    resultA = -1

if int(resultB) == 0:
    resultB = -1

print(resultB, end=' ')
print(resultA)
