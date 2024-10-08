"""
1463
1로 만들기
https://www.acmicpc.net/problem/1463
"""

n = int(input())
memo = [0] * (n + 1)

for i in range(2, n + 1):
    memo[i] = memo[i - 1] + 1
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i // 3] + 1)
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i // 2] + 1)
print(memo[-1])
