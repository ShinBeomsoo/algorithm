"""
21275
폰 호석만
silver 2
https://www.acmicpc.net/problem/21275
"""
digits = "0123456789abcdefghijklmnopqrstuvwxyz"

def possible_base(num):
    result_list = []
    for i in range(2, 36)
        result = ""
        while 1:
            remain = num % i
            result = (digits[remain]) + result
            num = num // i
            if num == 0:
                break
        result_list.append()
    return base


if __name__ == '__main__':
    num1, num2 = map(int, input().split(" "))
    print(num1, num2)
    binary = possible_base(num1)
    binary.reverse()
    print(binary)

a = []
a.append(1)