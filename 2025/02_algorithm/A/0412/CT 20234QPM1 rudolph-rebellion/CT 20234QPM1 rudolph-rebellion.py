N, M, P, C, D = map(int, input().split())
rx, ry = map(lambda x: int(x)-1, input().split())
santas = [0]*(P)
sarr = [[-1]*N for _ in range(N)]
die = [0]*P
stun = [-1]*P
ans = [0]*P

for _ in range(P):
    sidx, sx, sy = map(lambda x:int(x)-1, input().split())
    santas[sidx] = (sx, sy)
    sarr[sx][sy]=sidx

for turn in range(M):

    next_rodolph = (3*N**2, -rx, -ry)
    for i in range(P):
        if die[i]: continue
        sx, sy = santas[i]
        this_rodolph = (abs(sx-rx)**2+abs(sy-ry)**2, -sx, -sy)
        next_rodolph = min(this_rodolph, next_rodolph)

    nsx, nsy = -next_rodolph[1], -next_rodolph[2]
    drx, dry = 0, 0
    if rx<nsx: drx += 1
    elif rx>nsx: drx -= 1
    if ry<nsy: dry += 1
    elif ry>nsy: dry -= 1

    rx, ry = rx+drx, ry+dry
    if sarr[rx][ry]!=-1:
        sidx = sarr[rx][ry]
        stun[sidx]=turn+1
        sarr[rx][ry]=-1
        ans[sidx]+=C

        sx, sy = santas[sidx]
        nsx, nsy = sx+drx*C, sy+dry*C
        if not(0<=nsx<N and 0<=nsy<N):
            die[sidx]=1
        else:
            while True:
                santas[sidx]=(nsx, nsy)
                sarr[nsx][nsy], sidx = sidx, sarr[nsx][nsy]
                if sidx == -1 : break
                sx, sy = santas[sidx]
                nsx, nsy = sx+drx, sy+dry
                if not(0<=nsx<N and 0<=nsy<N):
                    die[sidx]=1
                    break

    nsarr= [[-1]*N for _ in range(N)]
    for i in range(P):
        if die[i] or stun[i]>=turn: continue

        sx, sy = santas[i]
        sarr[sx][sy]=-1
        dist, dsx, dsy = abs(rx-sx)**2+abs(ry-sy)**2, 0, 0
        for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nx, ny = sx+dx, sy+dy
            if not(0<=nx<N and 0<=ny<N) or sarr[nx][ny]!=-1: continue
            ndist = abs(rx-nx)**2+abs(ry-ny)**2
            if ndist<dist:
                dist, dsx, dsy = ndist, dx, dy

        nsx, nsy = sx+dsx, sy+dsy
        santas[i]=(nsx, nsy)
        sarr[nsx][nsy]=i
        if (nsx, nsy)==(rx, ry):
            sarr[nsx][nsy] = -1
            stun[i] = turn + 1
            ans[i] += D

            nsx, nsy = nsx - dsx * D, nsy - dsy * D
            if not (0 <= nsx < N and 0 <= nsy < N):
                die[i] = 1
            else:
                sidx = i
                while True:
                    santas[sidx] = (nsx, nsy)
                    sarr[nsx][nsy], sidx = sidx, sarr[nsx][nsy]
                    if sidx == -1: break
                    sx, sy = santas[sidx]
                    nsx, nsy = sx - dsx, sy - dsy
                    if not (0 <= nsx < N and 0 <= nsy < N):
                        die[sidx] = 1
                        break

    if sum(die)==P:
        break

    for i in range(P):
        if die[i]: continue
        ans[i]+=1
print(*ans)
