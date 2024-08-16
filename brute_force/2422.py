"""
2422
https://www.acmicpc.net/problem/2422
한윤정이 이탈리아에 가서 아이스크림을 사먹는데
"""
from itertools import combinations

n, m = map(int, input().split(' '))

forbidden_pairs = set()
for _ in range(m):
    u, v = map(int, input().split())
    forbidden_pairs.add((u, v))
    forbidden_pairs.add((v, u))

count = 0
for c in combinations(range(1, n+1), 3):
    if (c[0], c[1]) in forbidden_pairs or (c[0], c[2]) in forbidden_pairs or (c[1], c[2]) in forbidden_pairs:
        continue
    count += 1
print(count)

