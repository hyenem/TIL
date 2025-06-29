from collections import deque


def move(x, y, z, d):
    if (x, y, z, d) in warp:
        nx, ny, nz = warp[(x, y, z, d)]
        if mapp[nz][nx][ny]==1:
            return x, y, z
        return nx, ny, nz

    dx, dy = dxdy[d]
    if z==5:
        nx, ny, nz = x+dx, y+dy, 5
        if not(0<=nx<N and 0<=ny<N):
            return x, y, z
    else:
        nx, ny = x + dx, y + dy
        if 0<=nx<M and 0<=ny<M:
            nz = z
        else:
            if z==4:
                nx, nz = 0, d
                ny = (M-1-x, y, x, M-1-y)[d]
            else:
                if d==1:
                    return x, y, z
                elif d==3:
                    nz = 4
                    nx, ny = ((M-1-y, M-1), (M-1, y), (y, 0), (0, M-1-y))[z]
                elif d==0:
                    nx, ny, nz = x, 0, (z-1)%4
                else:
                    nx, ny, nz = x, M-1, (z+1)%4
    if mapp[nz][nx][ny]==1: return x, y, z
    else: return nx, ny, nz


N, M, F = map(int, input().split())
unknown = [list(map(int, input().split())) for _ in range(N)]
mapp = [[list(map(int, input().split())) for _ in range(M)] for _ in range(5)]+[unknown]
mapp[1], mapp[2] = mapp[2], mapp[1]
dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0))
warp = {}

sx, sy = -1, -1
for i in range(N):
    for j in range(N):
        if unknown[i][j]==4:
            ex, ey = i, j
        elif unknown[i][j]==3:
            if sx==-1:
                sx, sy = i, j

            for d in range(4):
                dx, dy = dxdy[d]
                nx, ny = i+dx, j+dy
                if not(0<=nx<N and 0<=ny<N) or unknown[nx][ny]==3: continue

                twx, twz = M-1, d
                twy = (M-1-(nx-sx), ny-sy, nx-sx, M-1-(ny-sy))[d]

                warp[(i, j, 5, (d+2)%4)]=(twx, twy, twz)
                warp[(twx, twy, twz, 1)] = (nx, ny, 5)

visited = [[[6*N*N]*M for _ in range(M)] for _ in range(5)]+[[[6*N*N]*N for _ in range(N)]]
changed = (0, 2, 1, 3)
for _ in range(F):
    x, y, d, v = map(int, input().split())
    d = changed[d]
    visited[5][x][y]=0
    dx, dy = dxdy[d]
    time = 0
    while 0<=x+dx<N and 0<=y+dy<N:
        time += v
        x, y = x+dx, y+dy
        if mapp[5][x][y]: break
        visited[5][x][y]=min(visited[5][x][y], time)

for i in range(M):
    for j in range(M):
        if mapp[4][i][j]==2:
            q = deque([(i, j, 4, 0)])
            visited[4][i][j]=0

while q:
    x, y, z, t = q.popleft()
    if (x, y, z) == (ex, ey, 5):
        print(t)
        break

    for d in range(4):
        nx, ny, nz = move(x, y, z, d)
        if mapp[nz][nx][ny]==1: continue
        if visited[nz][nx][ny]>t+1:
            visited[nz][nx][ny]=t+1
            q.append((nx, ny, nz, t+1))

else: print(-1)