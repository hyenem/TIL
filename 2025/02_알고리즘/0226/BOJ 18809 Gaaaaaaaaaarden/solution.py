from collections import deque


def blossom():
    global ans
    flower = 0
    visited = [ele[:] for ele in ovisited]
    q = deque(lst)
    nq = deque()

    while q:
        while q:
            t, c, x, y= q.popleft()
            if visited[x][y]==0:
                visited[x][y] = 2 * t + c
            elif visited[x][y]==-1: continue
            else :
                if visited[x][y] == 2 * t + 3 - c:
                    visited[x][y]=-1
                    flower +=1
                continue
            for dx, dy in ((0,1), (0, -1), (1, 0), (-1, 0)):
                nx, ny  =x+dx, y+dy
                if not (0<=nx<N and 0<=ny<M):continue
                if visited[nx][ny]==0:
                    nq.append((t+1, c, nx, ny, x, y))
        while nq:
            t, c, x, y, bx, by = nq.popleft()
            if visited[bx][by]==-1: continue
            q.append((t, c, x, y))

    ans = max(ans, flower)

def combination(cntG, cntR, idx):
    if cntG==G and cntR==R:
        blossom()
        return

    if idx==len(can): return
    
    if cntG<G:
        lst.append((0, 2, can[idx][0], can[idx][1]))
        combination(cntG+1, cntR, idx+1)
        lst.pop()
    if cntR<R:
        lst.append((0, 1, can[idx][0], can[idx][1]))
        combination(cntG, cntR+1, idx+1)
        lst.pop()
    combination(cntG, cntR, idx+1)
    

N, M, G, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
can = []
lst = []
ans = 0

ovisited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            ovisited[i][j]=-1
        elif arr[i][j]==2:
            can.append((i,j))

combination(0, 0, 0)

print(ans)