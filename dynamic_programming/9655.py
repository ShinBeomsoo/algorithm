"""
9655
돌 게임
https://www.acmicpc.net/problem/9655
"""
# 첫번째 풀이
# N = int(input())

# if N % 2 == 0:
#     print("CY")
# else:
#     print("SK")


# 두번째 풀이
N = int(input())
dp = [""] * (N + 2)

# 베이스 케이스 초기화
dp[1] = "SK"
if N >= 2:
    dp[2] = "CY"
if N >= 3:
    dp[3] = "SK"
if N >= 4:
    dp[4] = "SK"

# 동적 프로그래밍 진행
for i in range(5, N + 1):
    if dp[i - 1] == "CY" or dp[i - 3] == "CY":
        dp[i] = "SK"
    else:
        dp[i] = "CY"

# 결과 출력
print(dp[N])