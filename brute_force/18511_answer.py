ef sol(order, num):
    global final_ans

    if order == len(str(N)):
        if not '0' in str(num):
            final_ans = max(final_ans, num)
        return

    for i in range(K):
        now_num = arr[i]*(10**(len(str(N))-order-1)) + num

        if now_num <= N:
            sol(order + 1, now_num)

        else:
            sol(order+1, num)


N, K = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort(reverse=True)

final_ans= 0
sol(0, 0)

print(final_ans)
