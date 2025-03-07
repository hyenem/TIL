import heapq

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[0]*M for _ in range(N)]
DP[0][0]=1
q = [(-arr[0][0], 0, 0)]
while q:
    c, x, y = heapq.heappop(q)
    if c>=arr[N-1][M-1]: continue
    res = 0
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = x+dx, y+dy
        if not (0<=nx<N and 0<=ny<M): continue
        if arr[x][y]<arr[nx][ny]:
            res += DP[nx][ny]
        elif arr[nx][ny]<arr[x][y]:
            heapq.heappush(q, (-arr[nx][ny], nx, ny))
    if (x,y)!=(0, 0) :
        DP[x][y]=res

print(DP[N-1][M-1])