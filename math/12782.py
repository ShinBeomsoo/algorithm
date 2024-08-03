"""
12782
비트 우정지수
"""
test_case = int(input())
test_list = []
result = []
for _ in range(test_case):
    n, m = input().split(" ")
    test_list.append([n, m])

# 1. 1 0 의 개수를 맞춰야 한다.
for test in test_list:
    n, m = test
    count_1 = 0
    count_0 = 0
    for i in range(len(n)):
        if n[i] != m[i]:
            if n[i] == '1':
                count_1 += 1
            else:
                count_0 += 1
    result.append(max(count_1, count_0))
    print(count_1, count_0)
for r in result:
    print(r) 