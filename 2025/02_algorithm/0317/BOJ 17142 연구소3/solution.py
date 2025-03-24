from collections import deque


def bfs():
    global ans
    thisempty = empty
    dq = deque()
    visited = [[0]*N for _ in range(N)]
    for x, y in q:
        dq.append((0, x, y))
        visited[x][y]=1

    while dq:
        t, x, y = dq.popleft()
        if t>=ans: return
        if arr[x][y]==0:
            thisempty -= 1
            if thisempty ==0: break

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N): continue
            if arr[nx][ny] == 1: continue
            if visited[nx][ny]: continue
            visited[nx][ny] = 1
            dq.append((t+1, nx, ny))

    if thisempty==0:
        ans = t

def btk(idx, cnt):
    if cnt == M:
        bfs()
        return

    for i in range(idx, len(virus)):
        q.append(virus[i])
        btk(i+1, cnt+1)
        q.pop()


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
empty = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:
            virus.append((i, j))
        elif arr[i][j]==0:
            empty += 1

if empty ==0:
    print(0)
else :
    ans = N*N+1
    q = []
    btk(0, 0)
    if ans==N*N+1: ans = -1
    print(ans)