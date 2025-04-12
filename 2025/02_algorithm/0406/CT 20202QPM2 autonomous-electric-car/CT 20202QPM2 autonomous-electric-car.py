from collections import deque

def gotop():
    q = deque([(tx, ty)])
    visited = [[0]*N for _ in range(N)]
    visited[tx][ty]=1
    candidate = []
    cnt = 0
    while q:
        nq = deque()
        while q:
            x, y = q.popleft()
            if start[x][y]:
                candidate.append((x, y))

            if candidate: continue
            for dx, dy in dxdy:
                nx, ny = x+dx, y+dy
                if not(0<=nx<N and 0<=ny<N) or visited[nx][ny]: continue
                if arr[nx][ny]: continue
                visited[nx][ny]=1
                nq.append((nx, ny))

        if candidate:
            nx, ny = sorted(candidate)[0]
            return nx, ny, cnt

        q = nq
        cnt += 1

    return -1, -1, -1


def gotog(p):
    q = deque([(0, tx, ty)])
    visited = [[0] * N for _ in range(N)]
    visited[tx][ty] = 1
    while q:
        cnt, x, y = q.popleft()
        if (x, y)==(pdata[p-1][2]-1, pdata[p-1][3]-1):
            return x, y, cnt

        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny]: continue
            if arr[nx][ny]: continue
            visited[nx][ny] = 1
            q.append((cnt+1, nx, ny))

    return -1, -1, -1

dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
N, M, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tx, ty = map(lambda x: int(x)-1, input().split())
pdata = [list(map(int, input().split())) for _ in range(M)]
start = [[0]*N for _ in range(N)]
for i, (sx, sy, gx, gy) in enumerate(pdata, start = 1):
    start[sx-1][sy-1]=i

for _ in range(M):
    tx, ty, cnt= gotop()
    if cnt==-1 or C<=cnt:
        print(-1)
        break

    p = start[tx][ty]
    start[tx][ty]=0
    C -= cnt

    tx, ty, cnt = gotog(p)
    if cnt==-1 or C<cnt:
        print(-1)
        break
    C += cnt
else:
    print(C)