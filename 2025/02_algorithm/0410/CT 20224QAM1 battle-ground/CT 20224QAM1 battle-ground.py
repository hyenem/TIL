def pick(idx):
    x, y = player[idx][0], player[idx][1]
    arr[x][y].sort()
    if arr[x][y][-1]>player[idx][4]:
        arr[x][y][-1], player[idx][4] = player[idx][4], arr[x][y][-1]

N, M, K = map(int, input().split())
arr = [list(map(lambda x: [int(x)], input().split())) for _ in range(N)]
parr = [[0]*N for _ in range(N)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
player = [0]
ans = [0]*(M+1)
for _ in range(M):
    x, y, d, s = map(int, input().split())
    parr[x-1][y-1]=len(player)
    player.append([x-1, y-1, d, s, 0])

for _ in range(K):
    for i in range(1, M+1):
        px, py, pd, ps, pg = player[i]
        parr[px][py]=0
        dx, dy = dxdy[pd]
        if not (0<=px+dx<N and 0<=py+dy<N):
            pd = (pd+2)%4
            player[i][2]=pd
            dx, dy = dxdy[pd]

        px, py = px+dx, py+dy
        player[i][0], player[i][1] = px, py

        if parr[px][py]:
            ex, ey, ed, es, eg = player[parr[px][py]]
            if es+eg<ps+pg or (es+eg==ps+pg and es<ps):
                win, lose = i, parr[px][py]
            else: win, lose = parr[px][py], i

            wx, wy, wd, ws, wg = player[win]
            lx, ly, ld, ls, lg = player[lose]
            ans[win] += (ws+wg)-(ls+lg)

            if lg!=0:
                arr[lx][ly].append(lg)
                lg = 0
                player[lose][4]=0

            for _ in range(4):
                dx, dy = dxdy[ld]
                nx, ny = lx+dx, ly+dy
                if not (0 <= nx < N and 0 <= ny < N) or parr[nx][ny]:
                    ld = (ld+1)%4
                    player[lose][2] = ld
                    continue
                lx, ly = nx, ny
                player[lose][0], player[lose][1] = lx, ly
                break

            pick(lose)
            pick(win)
            parr[lx][ly] = lose
            parr[wx][wy] = win
        else:
            parr[px][py]=i
            pick(i)

ans = ans[1:]
print(*ans)