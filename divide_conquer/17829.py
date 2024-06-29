# 222-폴링

# 1. 입력받는다.
# 2. 2*2 정사각형을 각각 구한다.
# 3. 정사각형에서 가장 큰 수를 구한다.

size = int(input())
matrix = []  # mat도 괜찮음.
rectangle = []

for s in range(size):
    row = list(map(int, input().strip().split()))  # matrix_s -> row
    matrix.append(row)

curr_size = size
#TODO recursive function으로 구현
while curr_size > 1:
    new_matrix = []
    for i in range(0, curr_size, 2):
        new_row = []
        for j in range(0, curr_size, 2):
            #TODO sorted가 필요할까????? 필요없을 듯
            second_biggest_number = sorted(
                [
                    matrix[i][j],
                    matrix[i][j + 1],
                    matrix[i + 1][j],
                    matrix[i + 1][j + 1],
                ],
                reverse=True,
            )[1]
            new_row.append(second_biggest_number)
        new_matrix.append(new_row)
    matrix = new_matrix
    curr_size //= 2

print(new_matrix[0][0])
