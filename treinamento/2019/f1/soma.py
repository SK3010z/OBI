# N, K = map(int, input().split())
# X = list(map(int, input().split()))
# soma = 0
# for tamanho in range(N):
#     qtdOperacoes = N - tamanho
#     for i in range(qtdOperacoes):
#         Xi = X[i:i+tamanho+1]
#         s = sum(Xi)
#         if s == K:
#             soma += 1
#
# print(soma)
#
#
#

N, K = map(int, input().split())
X = list(map(int, input().split()))

# Dicionário para armazenar somas prefixadas e suas frequências
prefix_sums = {0: 1}
current_sum = 0
count = 0

for num in X:
    current_sum += num
    if current_sum - K in prefix_sums:
        count += prefix_sums[current_sum - K]
    if current_sum in prefix_sums:
        prefix_sums[current_sum] += 1
    else:
        prefix_sums[current_sum] = 1

print(count)