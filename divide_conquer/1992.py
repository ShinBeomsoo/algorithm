"""
1992. 쿼드트리
size는 2의 제곱수. 1<= <= 64
"""

# 1. 왼쪽위, 오른쪽위, 오른쪽아래, 왼쪽아래 순으로 나눈다.
# 2. 나눈 부분을 일반화한다.
# 3. 나눈 부분을 재귀로 돌린다.

size = int(input())
matrix = [list(map(int, input())) for _ in range(size)]

def divide(matrix, size):
    s = 0
    for m in matrix:
        s += sum(m)
    if s == 0:
        return "0"
    if s == size * size:
        return "1"

    size = size // 2
    return (
        "("
        + divide([m[:size] for m in matrix[:size]], size)
        + divide([m[size:] for m in matrix[:size]], size)
        + divide([m[:size] for m in matrix[size:]], size)
        + divide([m[size:] for m in matrix[size:]], size)
        + ")"
    )


print(divide(matrix, size))
