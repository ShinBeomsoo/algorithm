"""
10798
https://www.acmicpc.net/problem/10798
"""
lines = []
for _ in range(5):
    line = list(input().strip())
    while len(line) < 15:
        line.append("")
    lines.append(line)

for i in range(15):
    for j in range(5):
        if lines[j][i] != "":
            print(lines[j][i], end="")
