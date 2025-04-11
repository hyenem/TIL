N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
runner = [tuple(map(lambda x:int(x)-1, input().split())) for _ in range(M)]
ex, ey = map(lambda x:int(x)-1, input().split())

ans = 0
for _ in range(K):

    for i in range(len(runner)-1, -1, -1):
        rx, ry = runner[i]
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = rx+dx, ry+dy
            if not(0<=nx<N and 0<=ny<N): continue
            if arr[nx][ny]: continue
            if abs(nx-ex)+abs(ny-ey)>=abs(rx-ex)+abs(ry-ey): continue
            ans += 1
            if (nx, ny)==(ex, ey):
                del runner[i]
            else: runner[i]=(nx, ny)
            break
    if not runner: break

    rotate_data = (N+1, N+1, N+1)
    for rx, ry in runner:
        tside = max(abs(rx-ex), abs(ry-ey))+1
        mx, my = max(rx, ex), max(ry, ey)

        tsx, tsy = max(0, mx-tside+1), max(0, my-tside+1)
        rotate_data = min(rotate_data, (tside, tsx, tsy))

    side, sx, sy = rotate_data

    tmp = [ele[:] for ele in arr]
    for i in range(side):
        for j in range(side):
            arr[sx+i][sy+j]=max(0, tmp[sx+side-1-j][sy+i]-1)

    ex, ey = sx+ey-sy, sy+side-1-(ex-sx)
    for i in range(len(runner)):
        rx, ry = runner[i]
        if sx<=rx<sx+side and sy<=ry<sy+side:
            runner[i] = sx+ry-sy, sy+side-1-(rx-sx)

print(ans)
print(ex+1, ey+1)

