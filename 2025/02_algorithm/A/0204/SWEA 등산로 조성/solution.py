from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    q = deque()
    top = 0
    visited = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]>top:
                top = arr[i][j]
                visited = 0
                while q:
                    q.popleft()
            if arr[i][j]==top:
                # 각 좌표, 등산로의 길이, 지형 깎았는지, 이번에 높이가 얼만지, 이전에 있었던 곳이 어딘지
                q.append((i, j, 1, False, top, 1<<(i*N+j)))

    while q:
        x, y, cnt, used, now, visited =q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0<=nx<N and 0<=ny<N):
                continue
            if visited&(1<<nx*N+ny)!=0:
                continue
            if arr[nx][ny]<now:
                q.append((nx, ny, cnt+1, used, arr[nx][ny], visited|(1<<nx*N+ny)))
            else :
                if used:
                    continue
                if arr[nx][ny]-K<now:
                    q.append((nx, ny, cnt+1, True, now-1, visited|(1<<nx*N+ny)))
    print(f'#{tc} {cnt}')