"""
1969
DNA
https://www.acmicpc.net/problem/1969
"""
N, M = map(int, input().split())
dna_list = []
for _ in range(N):
    dna_list.append(input())

answer = ""
hamming_distance = 0

for m in range(M):
    dna_dict = {"A": 0, "T": 0, "G": 0, "C": 0}
    for n in range(N):
        # print(n, m)
        dna_dict[dna_list[n][m]] += 1
    # print(dna_dict)
    dna_answer = max(sorted(dna_dict), key=dna_dict.get)
    answer += dna_answer
    for dna, count in dna_dict.items():
        if dna != dna_answer:
            hamming_distance += count

print(answer)
print(hamming_distance)

