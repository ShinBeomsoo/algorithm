"""
1343
폴리오미노
"""

# 처음 답
board = input()
# O(n) O(n) O(n) => O(3n) => O(n)
if board.count("X") % 2 != 0:
    print(-1)
else:
    board = board.replace("XXXX", "AAAA")
    board = board.replace("XX", "BB")
    print(board)


# 최종 답
# O(2n) => O(n)
board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")
if 'X' in board:
    print(-1)
else:
    print(board)


