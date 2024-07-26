"""
문제: 4256
level: gold-2
"""
class Node:
    left = None
    root = None
    right = None

test_case = int(input())
print("test case: ", test_case)
for _ in range(test_case):
    number_node = int(input())
    preorder_result = input().split(" ")
    inorder_result = input().split(" ")
    print(preorder_result)
    print(inorder_result)

