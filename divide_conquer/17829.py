# 222-폴링

# 1. 입력받는다.
# 2. 2*2 정사각형을 각각 구한다.
# 3. 정사각형에서 가장 큰 수를 구한다.

size = int(input())
matrix = []
rectangle = []

for s in range(size):
    matrix_s = list(map(int, input().strip().split()))
    matrix.append(matrix_s)


while 1:
    new_matrix = []
    for i in range(0, size, 2):
        new_row = []
        for j in range(0, size, 2):
            max_number = sorted([matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]], reverse=True)[1]
            new_row.append(max_number)
        new_matrix.append(new_row)
    matrix = new_matrix
    size //= 2
    if size <= 1:
        break
print(new_matrix[0][0])

