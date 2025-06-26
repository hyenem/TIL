N, M, H, K = map(int, input().split())
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
sulle_xy = [(N//2, N//2)]
sulle_d = []
repeat = 1
d = -1
while True:
    repeat += 1
    d = (d+1)%4
    dx, dy = dxdy[d]
    for _ in range(repeat//2):
        nx, ny = sulle_xy[-1][0]+dx, sulle_xy[-1][1]+dy
        sulle_xy.append((nx, ny))
        sulle_d.append(d)
        if nx==ny==0:
            break
    else: continue
    break
sulle_xy = sulle_xy[1:]+sulle_xy[-2::-1]
sulle_d = sulle_d[1:]+[(d+2)%4 for d in sulle_d][::-1]+[0]

runner = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, d = map(int, input().split())
    runner[x-1][y-1][d]+=1

tree = [[0]*N for _ in range(N)]
for _ in range(H):
    x, y = map(int, input().split())
    tree[x-1][y-1]=1

ans = 0
sidx = 0
sx, sy, sd = N//2, N//2, 0
for turn in range(1,K+1):

    newrunner = [[[0]*4 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for d in range(4):
                if runner[i][j][d]==0: continue

                if abs(i-sx)+abs(j-sy)<=3:
                    nd = d
                    dx, dy = dxdy[nd]
                    nx, ny = i+dx, j+dy
                    if not(0<=nx<N and 0<=ny<N):
                        nd = (d+2)%4
                        dx, dy = dxdy[nd]
                        nx, ny = i+dx, j+dy

                    if (nx, ny)==(sx, sy):
                        newrunner[i][j][nd] += runner[i][j][d]
                    else:
                        newrunner[nx][ny][nd] += runner[i][j][d]
                else:
                    newrunner[i][j][d] += runner[i][j][d]
    runner = newrunner

    sx, sy = sulle_xy[sidx]
    sd = sulle_d[sidx]
    sidx = (sidx+1)%len(sulle_xy)

    dx, dy = dxdy[sd]
    for k in range(3):
        nx, ny = sx+dx*k, sy+dy*k
        if not(0<=nx<N and 0<=ny<N): break
        if tree[nx][ny]: continue
        ans += sum(runner[nx][ny])*turn
        runner[nx][ny]=[0]*4
print(ans)