from collections import deque

def rotate(x, y, d):
    qx, qy = (x//4)*4, (y//4)*4
    rx, ry = x%4, y%4
    for _ in range(d):
        rx, ry = ry, 3-rx
    return (qx+rx, qy+ry)

K = int(input())
arr = [list(input()) for _ in range(K*4)]
for i in range(4*K):
    for j in range(4*K):
        if arr[i][j]=='S':
            sx, sy = i, j
        elif arr[i][j]=='E':
            ex, ey = i, j

q = deque([(0, 0, sx, sy)])
visited = [[[0, 0, 0, 0] for _ in range(4*K)] for _ in range(4*K)]
visited[sx][sy][0]=1
while q:
    t, rcnt, x, y = q.popleft()
    if (ex, ey) == (x, y):
        print(t)
        break

    for dx, dy in ((0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)):
        nx, ny = x+dx, y+dy
        if not(0<=nx<4*K and 0<=ny<4*K) or (x//4, y//4)!=(nx//4, ny//4):
            continue
        if arr[nx][ny]=='#': continue
        nrcnt = (rcnt+1)%4
        if visited[nx][ny][nrcnt]: continue
        visited[nx][ny][nrcnt] = 1
        q.append((t+1, nrcnt, nx, ny))

    rx, ry = rotate(x, y, rcnt)
    for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nrx, nry = rx+dx, ry+dy
        if not(0<=nrx<4*K and 0<=nry<4*K) or (x//4, y//4)==(nrx//4, nry//4):
            continue
        if arr[nrx][nry]=='#': continue
        nrcnt = 1
        if visited[nrx][nry][nrcnt]: continue
        visited[nrx][nry][nrcnt] = 1
        q.append((t + 1, nrcnt, nrx, nry))

else : print(-1)