"""
2839
설탕배달
https://www.acmicpc.net/problem/2839
"""

N = int(input())

dp = [0] * 5001 

dp[0] = 0
dp[1] = -1
dp[2] = -1
dp[3] = 1
dp[4] = -1
dp[5] = 1

for i in range(6, N + 1):
    if dp[i-3] != -1:
        dp[i] = min(dp[i-3], dp[i-5]) + 1
    if dp[i-5] != -1:
        dp[i] = min(dp[i-3], dp[i-5]) + 1

print(dp[N])
