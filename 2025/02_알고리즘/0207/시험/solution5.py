from collections import deque
dx=(-1, 1, 0, 0)
dy = (0, 0, -1, 1)
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    people = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                people += 1
    q = deque()
    sx, sy = map(lambda x: int(x)-1,input().split())
    q.append((1, sx, sy))
    arr[sx][sy]=0
    people -=1
    while q:
        cnt, x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<M and arr[nx][ny]==1:
                arr[nx][ny]=0
                people -=1
                q.append((cnt+1, nx, ny))
    print(f'#{tc} {cnt} {people}')
