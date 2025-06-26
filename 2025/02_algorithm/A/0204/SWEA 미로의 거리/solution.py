T = int(input())
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    q=[]
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]==2:
                q.append((0, i, j))
    while q:
        c, x, y = q.pop(0)
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny]==3:
                    ans = c
                    break
                elif arr[nx][ny]==0:
                    arr[nx][ny]=1
                    q.append((c+1, nx, ny))
    print(f'#{tc} {ans}')
