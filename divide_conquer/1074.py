"""
1074 Z 탐색
z 서치에 너무 많은 시간을 할애하였다.
"""
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


"""
--------------------------------------------------------
정답
시간복잡도: O(logN) => 매트릭스가 계속 반으로 줄어든다.
"""
N, r, c = map(int, input().split())

count = 0

while N != 0:
    N -= 1
    # 1사분면
    if r < 2**N and c < 2**N:
        count += (2**N) * (2**N) * 0  # 2^N * 2^N * 0
    # 2사분면
    elif r < 2**N and 2**N <= c:
        count += (2**N) * (2**N) * 1
        c -= 2**N
        pass
    # 3분면
    elif 2**N <= r and c < 2**N:
        count += (2**N) * (2**N) * 2
        r -= 2**N
    # 4분면
    else:
        count += (2**N) * (2**N) * 3
        r -= 2**N
        c -= 2**N
print(count)
