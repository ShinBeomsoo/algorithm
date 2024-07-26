"""
9342
A~Z
"""
def check1(word):
    return word[0] in {'A', 'B', 'C', 'D', 'E', 'F'}

def check2(word):
    flag1 = flag2 = flag3 = False

    for i, char in enumerate(word):
        if i > 0 and char not in {'A', 'F', 'C'}:
            return False

        if char == 'A':
            flag1 = True
        elif char == 'F' and flag1:
            flag2 = True
        elif char == 'C' and flag1 and flag2:
            flag3 = True

    return flag3

def check3(word):
    return word[-1] in {'A', 'B', 'C', 'D', 'E', 'F'}

def main():
    t = int(input())
    for _ in range(t):
        word = input().strip()
        if check1(word) and check2(word) and check3(word):
            print("Infected!")
        else:
            print("Good")

if __name__ == "__main__":
    main()
