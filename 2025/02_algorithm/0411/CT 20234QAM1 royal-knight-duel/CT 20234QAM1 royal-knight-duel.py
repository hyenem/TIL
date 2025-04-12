from collections import deque

L, N, Q = map(int, input().split())
die = [0]*N
knights = [0]
arr = [list(map(int, input().split())) for _ in range(L)]
for _ in range(N):
    x, y, h, w, k = map(int, input().split())
    knights.append((x-1, y-1, h, w, k))

dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
cmds = [tuple(map(int, input().split())) for _ in range(Q)]

karr= [[0]*L for _ in range(L)]
for idx, (x, y, h, w, k) in enumerate(knights[1:], start=1):
    for i in range(x, x+h):
        for j in range(y, y+w):
            karr[i][j]=idx

ans = [0]*(N+1)
for ki, kd in cmds:
    if knights[ki][4]<=0: continue
    dx, dy = dxdy[kd]

    visited = [0]*(N+1)
    q = [ki]
    visited[ki]=1
    qidx = 0
    while qidx<len(q):
        idx = q[qidx]
        qidx+=1
        x, y, h, w, k = knights[idx]
        nx, ny = x+dx, y+dy
        for i in range(nx, nx+h):
            for j in range(ny, ny+w):
                if not(0<=i<L and 0<=j<L) or arr[i][j]==2:
                    break
                if karr[i][j] != 0 and not visited[karr[i][j]]:
                    visited[karr[i][j]] = 1
                    q.append(karr[i][j])
            else: continue
            break
        else:
            continue
        q = []
        break

    for i in q:
        x, y, h, w, k = knights[i]
        knights[i]=[x+dx, y+dy, h, w, k]

    karr = [[0] * L for _ in range(L)]
    if q: q.pop(0)
    for idx in range(1, N+1):
        x, y, h, w, k = knights[idx]
        if idx in q:
            for i in range(x, x + h):
                for j in range(y, y + w):
                    if arr[i][j]==1:
                        ans[idx]+=1
                        knights[idx][4]-=1

        if knights[idx][4]<=0: continue

        for i in range(x, x + h):
            for j in range(y, y + w):
                karr[i][j]=idx

res = 0
for i in range(1, N+1):
    if knights[i][4]>0:
        res+=ans[i]

print(res)
