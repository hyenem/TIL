T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if abs(N//2-i)+abs(N//2-j)<=N//2:
                ans += arr[i][j]
    print(f'#{tc} {ans}')