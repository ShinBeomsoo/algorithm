"""
1074 Z 탐색
"""

N = int(input())  # N는 1<= <=15
r = int(input())
c = int(input())

# 4분할로 나누는 함수
# z로 탐색하는 함수
# 탐색하는 과정에서 숫자를 채워놓자!
# 원하는 행렬의 값을 matrix[r][c]로 구하자!


def z_search(position, r, c):
    position_r, position_c = position
    # 찾았다!
    if position_r == r and position_c == c:
        return 0
    else:
        # 처음
        print(position_r, position_c)
        # 오른쪽
        print(position_r, position_c + 1)
        # 왼쪽 아래
        print(position_r + 1, position_c)
        # 오른쪽 아래
        print(position_r + 1, position_c + 1)
    pass


def count_row_col(count, position, r, c):
    print(count, position, r, c)
    z_search(position, r, c)
    return count


def main(r, c):
    size = 2**N
    matrix = []
    # 왼쪽 위
    if 0 <= r < 2 ** (N - 1) and 0 <= c < 2 ** (N - 1):
        count = count_row_col(
            0,
            (0, 0),
            r,
            c,
        )
    # 오른쪽 위
    elif 0 <= r < 2 ** (N - 1) and 2 ** (N - 1) <= c < 2**N:
        count = count_row_col(
            2 ** (2 * N - 2),
            (0, 2 ** (N - 1)),
            r,
            c,
        )
    # 왼쪽 아래
    elif 2 ** (N - 1) <= r < 2**N and 0 <= c < 2 ** (N - 1):
        count = count_row_col(
            2 ** (2 * N - 2) * 2,
            (2 ** (N - 1), 0),
            r,
            c,
        )
    # 오른쪽 아래
    elif 2 ** (N - 1) <= r < 2**N and 2 ** (N - 1) <= c < 2**N:
        count = count_row_col(
            2 ** (2 * N - 2) * 3,
            (2 ** (N - 1), 2 ** (N - 1)),
            r,
            c,
        )
    else:
        print("error")
    return count


count = main(r, c)
print(count)
