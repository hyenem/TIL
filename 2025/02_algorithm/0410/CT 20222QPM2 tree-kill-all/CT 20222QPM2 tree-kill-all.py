N, M, K, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
killer = [[-1]*N for _ in range(N)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))

ans = 0
for t in range(M):

    tmp = [ele[:] for ele in arr]
    for i in range(N):
        for j in range(N):
            if tmp[i][j] == -1: continue
            if tmp[i][j] == 0: continue

            empty = []
            for dx, dy in dxdy:
                nx, ny = i+dx, j+dy
                if not(0<=nx<N and 0<=ny<N): continue
                if tmp[nx][ny]==-1 or killer[nx][ny]>=t: continue
                if tmp[nx][ny]==0:
                    empty.append((nx, ny))
                else:
                    tmp[i][j]+=1
                    arr[i][j]+=1

            for x, y in empty:
                arr[x][y] += tmp[i][j]//len(empty)

    kcnt, kx, ky, kstack = -1, -1, -1, []
    for i in range(N):
        for j in range(N):
            if arr[i][j]==-1: continue

            tmpcnt = 0
            tmpstack = []
            if arr[i][j]!=0:
                tmpstack.append((i, j))
                tmpcnt += arr[i][j]
                for dx, dy in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                    for k in range(1, K+1):
                        nx, ny = i+k*dx, j+k*dy
                        if not(0<=nx<N and 0<=ny<N) or arr[nx][ny]==-1: break

                        tmpstack.append((nx, ny))
                        tmpcnt+=arr[nx][ny]
                        if arr[nx][ny]==0: break

            if kcnt<tmpcnt:
                kcnt, kx, ky, kstack = tmpcnt, i, j, tmpstack

    ans += kcnt
    for x, y in kstack:
        arr[x][y]=0
        killer[x][y]=t+C

print(ans)