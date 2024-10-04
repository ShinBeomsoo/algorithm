"""
16439
치킨치킨치킨
https://www.acmicpc.net/problem/16439
"""
from itertools import combinations

N, M = map(int, input().split())
# 치킨 선호도
I = [list(map(int, input().split())) for _ in range(N)]

answer = 0

# 치킨 조합
combi = list(combinations([i for i in range(M)], 3))
for c in combi:
    total = 0
    for i in range(N):
        total = total + max(I[i][c[0]], I[i][c[1]], I[i][c[2]])
    if total > answer:
        answer = total

print(answer)
