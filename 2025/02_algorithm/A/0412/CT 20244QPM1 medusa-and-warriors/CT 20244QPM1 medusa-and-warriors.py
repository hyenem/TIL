from collections import deque

N, M = map(int, input().split())
sx, sy, ex, ey = map(int, input().split())
dxdy = ((-1, 0), (1, 0), (0, -1), (0, 1))

wdata = list(map(int, input().split()))
warr = [[0]*N for _ in range(N)]
for i in range(M):
    warr[wdata[2*i]][wdata[2*i+1]] += 1

arr = [list(map(int, input().split())) for _ in range(N)]

q = deque([(sx, sy, [])])
arr[sx][sy]=1
medusa = 0
while q:
    x, y, root = q.popleft()
    if (x, y)==(ex, ey):
        medusa = root
        break

    for dx, dy in dxdy:
        nx, ny = x+dx, y+dy
        if not(0<=nx<N and 0<=ny<N): continue
        if arr[nx][ny]: continue
        arr[nx][ny]=1
        q.append((nx, ny, root+[(nx, ny)]))

if not medusa:
    print(-1)
else:
    medusa.pop()
    for mx, my in medusa:
        ans = [0] * 3
        warr[mx][my] = 0

        cnt = -1
        sarea = []
        for dx, dy in dxdy:

            tmpcnt = 0
            q = [(mx, my)]
            qidx = 0
            visited = [[0]*N for _ in range(N)]
            if dx==0: ndxdy = ((-1, dy), (0, dy), (1, dy))
            else : ndxdy = ((dx, -1), (dx, 0), (dx, 1))

            while qidx<len(q):
                x, y = q[qidx]
                qidx += 1

                for ndx, ndy in ndxdy:
                    nx, ny = x+ndx, y+ndy
                    if not(0<=nx<N and 0<=ny<N): continue
                    if visited[nx][ny]: continue
                    q.append((nx, ny))
                    visited[nx][ny]=1
                    if warr[nx][ny]:
                        tmpcnt+=warr[nx][ny]
                        nq = deque([(nx, ny)])
                        if dx==0:
                            if mx>nx: wdxdy = ((-1, dy), (0, dy))
                            elif mx<nx: wdxdy = ((1, dy), (0, dy))
                            else: wdxdy = ((0, dy),)
                        else:
                            if my>ny: wdxdy = ((dx, -1), (dx, 0))
                            elif my<ny: wdxdy = ((dx, 1), (dx, 0))
                            else: wdxdy = ((dx, 0),)

                        while nq:
                            wx, wy = nq.popleft()
                            for wdx, wdy in wdxdy:
                                nwx, nwy = wx+wdx, wy+wdy
                                if not(0<=nwx<N and 0<=nwy<N): continue
                                if visited[nwx][nwy]: continue
                                visited[nwx][nwy]=1
                                nq.append((nwx, nwy))

            if cnt<tmpcnt:
                cnt = tmpcnt
                sarea = q


        ans[1]+=cnt
        stare = [[0]*N for _ in range(N)]
        for x, y in sarea[1:]:
            stare[x][y]=1

        nwarr = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if warr[i][j]==0: continue
                if stare[i][j]==1:
                    nwarr[i][j] += warr[i][j]
                    continue

                nx, ny = i, j
                for dx, dy in dxdy:
                    tnx, tny = nx+dx, ny+dy
                    if not(0<=tnx<N and 0<=tny<N): continue
                    if stare[tnx][tny]: continue
                    if abs(nx-mx)+abs(ny-my)<=abs(tnx-mx)+abs(tny-my): continue
                    nx, ny = tnx, tny
                    break

                for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                    tnx, tny = nx+dx, ny+dy
                    if not(0<=tnx<N and 0<=tny<N): continue
                    if stare[tnx][tny]: continue
                    if abs(nx-mx)+abs(ny-my)<=abs(tnx-mx)+abs(tny-my): continue
                    nx, ny = tnx, tny
                    break

                ans[0]+= warr[i][j]*(abs(i-nx)+abs(j-ny))
                if (nx, ny)!=(mx, my):
                    nwarr[nx][ny] += warr[i][j]
                else:
                    ans[2] += warr[i][j]
        warr = nwarr
        print(*ans)

    print(0)