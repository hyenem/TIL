def calculate(lst, idx, acc):
    global ans
    ans = max(ans, sum(map(lambda x: x**2, selected)))

    for i in range(idx, M):
        if acc+lst[i]<=C:
            selected.append(lst[i])
            calculate(lst, i+1, acc+lst[i])
            selected.pop()
    return

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    selected = []

    totans = 0
    for i in range(N*N):
        x1, y1 = i//N, i%N
        if y1>N-M: continue
        lst1 = arr[x1][y1:y1+M]
        ans = 0
        calculate(lst1, 0, 0)
        ans1 = ans

        for j in range(i+M, N*N):
            x2, y2 = j // N, j % N
            if y2>N-M: continue
            lst2 = arr[x2][y2:y2+M]
            ans = 0
            calculate(lst2, 0, 0)
            ans2 = ans

            totans = max(totans, ans1+ans2)

    print(f'#{tc} {totans}')


