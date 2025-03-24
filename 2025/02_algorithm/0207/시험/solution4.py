import heapq

T = int(input())
dx=(-1, 1, 0, 0)
dy = (0, 0, -1, 1)

for tc in range(1, T+1):
    N = int(input())
    sx, sy, gx, gy = map(int, input().split())
    arr=[list(map(int, input())) for _ in range(N)]
    ans = 9*N*N
    q = []
    heapq.heappush(q, (arr[sx][sy], sx, sy))
    visited = [[-1]*N for _ in range(N)]
    visited[sx][sy]=arr[sx][sy]
    while q:
        cnt, x, y = heapq.heappop(q)
        if (x, y)==(gx, gy):
            break
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny]==-1 or visited[nx][ny]>cnt+arr[nx][ny]:
                    visited[nx][ny]=cnt+arr[nx][ny]
                    heapq.heappush(q, (cnt+arr[nx][ny], nx, ny))
    print(f'#{tc} {cnt}')