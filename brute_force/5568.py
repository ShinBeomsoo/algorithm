"""
5568
카드 놓기
https://www.acmicpc.net/problem/5568
"""

from itertools import permutations

n = int(input())
k = int(input())

numbers = []
for _ in range(n):
    numbers.append(input())

answer = set()
for i in permutations(numbers, k):
    answer.add(int(''.join(i)))
print(len(answer))
