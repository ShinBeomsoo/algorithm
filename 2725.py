"""
2725
보이는 점의 개수
https://www.acmicpc.net/problem/2725
"""

test_case = int(input())
coordinate_list = []
dp_seeing_point = [0, 1, 1, 2, 2, 4]  # 문제에서 제시한 리스트


def get_divisor(N):
    N_divisor = []
    for i in range(1, N + 1):
        if N % i == 0:
            N_divisor.append(i)
    N_divisor.pop()
    return N_divisor


for i in range(test_case):
    N = int(input())
    coordinate_list.append(N)

biggest_coordinate = max(coordinate_list)
for i in range(6, biggest_coordinate + 1):
    c = 0
    for j in get_divisor(i):
        c += dp_seeing_point[j]
    dp_seeing_point.append(i-c)
# print(dp_seeing_point)

for coordinate in coordinate_list:
    count = 0
    for i in range(coordinate + 1):
        count += dp_seeing_point[i]
    print(count * 2 + 1)
