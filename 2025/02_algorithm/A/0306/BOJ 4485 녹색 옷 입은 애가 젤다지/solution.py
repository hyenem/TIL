import heapq
tc = 0
while True:
    tc+=1
    N = int(input())
    if N==0: break

    arr = [list(map(int, input().split())) for _ in range(N)]
    q = [(arr[0][0], 0, 0)]
    visited = [[-1]*N for _ in range(N)]
    visited[0][0]=arr[0][0]

    while q:
        c, x, y = heapq.heappop(q)
        if x==y==N-1:
            print(f'Problem {tc}: {c}')
            break
        if visited[x][y]!=-1 and visited[x][y]<c: continue
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x+dx, y+dy
            if not (0<=nx<N and 0<=ny<N): continue
            if visited[nx][ny]==-1 or visited[nx][ny]>c+arr[nx][ny]:
                visited[nx][ny]=c+arr[nx][ny]
                heapq.heappush(q, (visited[nx][ny], nx, ny))
