try:
    while True:
        s_str, t_str = input().split()
        i=0
        cnt = 0
        while i<len(s_str):
            for j in range(len(t_str)):
                if t_str[j] ==s_str[i]:
                    cnt =cnt+1
                    i=i+1
        if cnt == len(s_str) :
            print("Yes")
        else :
            print("No")
except Exception as error:
    print(error)
    break
