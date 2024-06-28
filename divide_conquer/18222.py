# 투에모스 문자열
"""
x와 x'
x+x' = x
2, 3 과정 반복
0 -> 01 -> 0110
"""

k = int(input())
k_ = len(bin(k)[2:])

a = '0'
b = bin(int(a, 2) ^ int(len(a)*'1', 2))

count = 0
while 1:
    if count == k_+1:
        break
    a = a+b[2:]
    b = bin(int(a, 2) ^ int(len(a)*'1', 2))
    count += 1
# print(a)
# print(a[k-1])

