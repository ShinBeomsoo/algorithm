"""
15650
N과 M (2)
https://www.acmicpc.net/problem/15650
"""
from itertools import combinations

n, k = map(int, input().split())
n = [i + 1 for i in range(n)]

ans = combinations(n, k)
for a in ans:
    print(*a)
