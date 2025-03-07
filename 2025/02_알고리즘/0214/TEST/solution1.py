dxdy = ((1,0),(0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1))

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr= [[0]*(M+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0]*(M+2)]
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i][j]==0:
                continue
            tmp = 0
            for dx, dy in dxdy:
                nx, ny = i+dx, j+dy
                if arr[nx][ny]!=0:
                    tmp+=1
            ans+=min(tmp, K)
    print(f'#{tc} {ans}')