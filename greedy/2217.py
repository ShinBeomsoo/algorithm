"""
2217 로프
"""
n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort()
res = rope[0] * n

k = n
for i in range(1,n):
    k = k-1
    if rope[i] != rope[i-1]:
        if res <= rope[i] * k:
            res = rope[i] *k

print(res)
