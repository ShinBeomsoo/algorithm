"""
18511
큰 수 구성하기
https://www.acmicpc.net/problem/18511
"""
N, K = map(int, input().split(" "))
N_length = len(str(N))
K_list = [int(k) for k in input().split(" ")]
K_list.sort(reverse=True)

answer = 0
found = False

for num in range(N_length, -1, -1):
    big_num = 0
    for k in K_list:
        n = k * (10**num) + answer
        if n <= N:
            big_num = k * (10**num)
            found = True
            break
    answer += big_num
    if found:
        break

print(answer)
if answer == 0:
    answer = K_list[-1]

print(answer)

