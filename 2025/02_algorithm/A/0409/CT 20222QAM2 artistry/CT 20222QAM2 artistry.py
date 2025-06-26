def bfs():
    global ans
    cnt = [0]
    visited = [[0]*N for _ in range(N)]
    color = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue

            cidx = len(cnt)
            visited[i][j]=1
            color[i][j]=cidx
            q = [(i, j)]
            idx = 0
            stack = []

            while idx<len(q):
                x, y = q[idx]
                idx += 1
                for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    nx, ny = x+dx, y+dy
                    if not(0<=nx<N and 0<=ny<N): continue
                    if arr[i][j]==arr[nx][ny]:
                        if not visited[nx][ny]:
                            visited[nx][ny]=1
                            color[nx][ny]=cidx
                            q.append((nx, ny))
                        continue
                    if color[nx][ny]==0: continue
                    else:
                        stack.append(color[nx][ny])
            cnt.append((arr[i][j], len(q)))
            for c in stack:
                ans += (len(q)+cnt[c][1])*arr[i][j]*cnt[c][0]

def rotate():
    tmp = [ele[:] for ele in arr]
    for i in range(N):
        arr[i][N//2]=tmp[N//2][N-1-i]
    for j in range(N):
        arr[N//2][j]=tmp[j][N//2]

    for sx in (0, N//2+1):
        for sy in (0, N//2+1):
            for i in range(N//2):
                for j in range(N//2):
                    arr[sx+i][sy+j]=tmp[sx+N//2-1-j][sy+i]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
bfs()
for _ in range(3):
    rotate()
    bfs()
print(ans)