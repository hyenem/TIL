import heapq

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

q = [(max(arr[0][0], arr[N-1][N-1])-min(arr[0][0], arr[N-1][N-1]), min(arr[0][0], arr[N-1][N-1]), max(arr[0][0], arr[N-1][N-1]), 0, 0)]
visited = [[[-1]*201 for _ in range(N)]*N for _ in range(N)]
visited[0][0][q[0][2]]=q[0][1]

while q:
    d, m, M, x, y = heapq.heappop(q)
    if x==N-1 and y==N-1:
        print(d)
        break

    for dx, dy in ((0,1), (0, -1), (-1, 0), (1, 0)):
        nx, ny =x+dx, y+dy
        if not(0<=nx<N and 0<=ny<N): continue
        if m>arr[nx][ny]:
            nm = arr[nx][ny]
            nM = M
        elif M<arr[nx][ny]:
            nm = m
            nM = arr[nx][ny]
        else :
            nm = m
            nM = M
        if visited[nx][ny][nM]==-1 or visited[nx][ny][nM]<nm:
            visited[nx][ny][nM]=nm
            heapq.heappush(q, (nM-nm, nm, nM, nx, ny))

