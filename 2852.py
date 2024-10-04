"""
2852
NBA 농구
https://www.acmicpc.net/problem/2852
3
1 01:10
2 21:10
2 31:30

20:00
16:30

1번팀: 
2번팀: 01:10 + (48:00 - 21:10) = 01:10 + 26:50 = 28:00
"""

total_time = 48 * 60
N = int(input())
team_score = []
team_score_1 = 0
team_score_2 = 0
team_time_1 = 0
team_time_2 = 0
team_time = []

for i in range(N):
    t, s = input().split()
    mm, ss = map(int, s.split(":"))
    mm_to_ss = mm * 60
    ss = mm_to_ss + ss
    team_score.append(int(t))
    team_time.append(ss)

team_time.insert(0, 0)
team_time.insert(len(team_time), total_time)
team_real_time = []

for i in range(0, len(team_time) - 1):
    a = team_time[i + 1] - team_time[i]
    team_real_time.append(a)


for i in range(N):
    if team_score[i] == 1:
        team_score_1 += 1
    else:
        team_score_2 += 1

    if team_score_1 > team_score_2:
        team_time_1 += team_real_time[i + 1]
    elif team_score_1 < team_score_2:
        team_time_2 += team_real_time[i + 1]
    else:
        pass

print(f"{team_time_1 // 60:02d}:{team_time_1 % 60:02d}")
print(f"{team_time_2 // 60:02d}:{team_time_2 % 60:02d}")
