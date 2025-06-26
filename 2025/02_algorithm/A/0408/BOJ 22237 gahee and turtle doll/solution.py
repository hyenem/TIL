from collections import deque

dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
direction = ['U', 'R', 'D', 'L']
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

turtle = []
w = []
for i in range(N):
    for j in range(M):
        if arr[i][j]=='T':
            tsx, tsy = i, j
            minx, maxx, miny, maxy = i, i, j, j
            q = deque([(i, j)])
            arr[i][j]='.'
            turtle.append((0, 0))
            while q:
                x, y = q.popleft()
                minx, maxx = min(minx, x), max(maxx, x)
                miny, maxy = min(miny, y), max(maxy, y)
                for dx, dy in dxdy:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<N and 0<=ny<M and arr[nx][ny]=='T':
                        arr[nx][ny]='.'
                        turtle.append((nx-i, ny-j))
                        q.append((nx, ny))
        elif arr[i][j]=='H':
            hx, hy = i, j
        elif arr[i][j]=='#':
            w.append((i, j))
home = set()
wall = set()
for tx, ty in turtle:
    home.add((hx-tx, hy-ty))
    for wx, wy in w:
        wall.add((wx-tx, wy-ty))

if miny<tsy:
    for i in range(N):
        for j in range(tsy-miny):
            wall.add((i, j))
for i in range(N):
    for j in range(M-(maxy-tsy), M):
        wall.add((i, j))

for i in range(N-(maxx-tsx), N):
    for j in range(M):
        wall.add((i, j))

q = deque([(tsx, tsy, '')])
visited = [[0]*M for _ in range(N)]
visited[tsx][tsy]=1
while q:
    x, y, root = q.popleft()
    if (x, y) in home:
        print(root)
        break
    for d in range(4):
        dx, dy = dxdy[d]
        nx, ny = x+dx, y+dy
        if not(0<=nx<N and 0<=ny<N): continue
        if (nx, ny) in wall: continue
        if visited[nx][ny]: continue

        visited[nx][ny]=1
        q.append((nx, ny, root+direction[d]))
else:
    print(-1)