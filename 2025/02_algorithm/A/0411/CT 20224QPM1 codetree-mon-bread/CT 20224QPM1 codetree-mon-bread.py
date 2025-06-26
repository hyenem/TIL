from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
people = []
block = [[0]*N for _ in range(N)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))

t = 0
cnt = 0
while True:
    t+=1
    for i, (sx, sy, ex, ey) in enumerate(people):
        q = deque([(sx, sy, -1)])
        visited = [[0]*N for _ in range(N)]
        visited[sx][sy]=1
        while q:
            x, y, sd = q.popleft()
            if (x, y)==(ex, ey):
                dx, dy =dxdy[sd]
                people[i]=(sx+dx, sy+dy, ex, ey)
                break

            for d in (0, 3, 1, 2):
                dx, dy = dxdy[d]
                nx, ny = x+dx, y+dy
                if not(0<=nx<N and 0<=ny<N) or block[nx][ny] or visited[nx][ny]:continue
                visited[nx][ny]=1
                if sd==-1:
                    q.append((nx, ny, d))
                else: q.append((nx, ny, sd))

    for i in range(len(people)-1, -1, -1):
        sx, sy, ex, ey = people[i]
        if (sx, sy)==(ex, ey):
            block[ex][ey]=1
            cnt+=1
            del people[i]

    if cnt==M:
        print(t)
        break

    if t<=M:
        x, y = map(int, input().split())
        ex, ey = x-1, y-1
        q = [(x-1, y-1)]
        visited = [[0]*N for _ in range(N)]
        visited[x-1][y-1]=1
        candidate = []
        while q:
            nq = []
            while q:
                x, y = q.pop()
                if arr[x][y]:
                    candidate.append((x, y))

                if candidate: continue

                for dx, dy in dxdy:
                    nx, ny = x+dx, y+dy
                    if not(0<=nx<N and 0<=ny<N): continue
                    if block[nx][ny]: continue
                    if visited[nx][ny]: continue
                    visited[nx][ny]=1
                    nq.append((nx, ny))

            if candidate:
                sx, sy = sorted(candidate)[0]
                arr[sx][sy]=0
                block[sx][sy]=1
                people.append((sx, sy, ex, ey))
                break
            q = nq
