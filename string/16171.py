"""
16171
나는 친구가 적다
"""
S = input()
K = input()
count = 0

s_alphabet = ""
for s in S:
    if s.isalpha():
        s_alphabet += s

if K in s_alphabet:
    print(1)
else:
    print(0)
