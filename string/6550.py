"""
6559
부분 문자열
"""
result = []
try:
    while True:
        line = input().strip()
        if not line:
            break
        s, t = line.split()
        word_index = 0

        for t_alphabet in t:
            if len(s) == word_index:
                break
            if s[word_index] == t_alphabet:
                word_index += 1
        if len(s) == word_index:
            result.append("Yes")
        else:
            result.append("No")
except EOFError:
    pass
for res in result:
    print(res)
