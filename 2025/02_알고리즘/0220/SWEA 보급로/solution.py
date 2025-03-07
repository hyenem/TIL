import heapq

T = int(input())
dxdy = ((1,0), (-1, 0), (0,-1), (0, 1))
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited =[[-1]*N for _ in range(N)]
    q=[(0,0,0)]
    visited[0][0]=0
    ans = 0
    while q:
        t, x, y = heapq.heappop(q)
        if x==N-1 and y==N-1:
            ans = t
            break
        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if not (0<=nx<N and 0<=ny<N):continue
            if visited[nx][ny]==-1 or visited[nx][ny]>t+arr[nx][ny]:
                visited[nx][ny]=t+arr[nx][ny]
                heapq.heappush(q, (visited[nx][ny], nx, ny))
    print(f'#{tc} {ans}')