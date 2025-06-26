def btk(acc, tmproot):
    global mcnt, root
    if len(tmproot)==3:
        if acc>mcnt:
            mcnt = acc
            root = tmproot
        return

    if tmproot:x, y = tmproot[-1]
    else: x, y = px, py
    for d in range(0, 8, 2):
        dx, dy = dxdy[d]
        nx, ny = x+dx, y+dy
        if not(0<=nx<4 and 0<=ny<4): continue
        if (nx, ny) in tmproot:
            nacc = acc
        else:
            nacc = acc+sum(arr[nx][ny])
        btk(nacc, tmproot+[(nx, ny)])

M, T = map(int, input().split())
px, py = map(lambda x: int(x)-1, input().split())
arr = [[[0]*8 for _ in range(4)] for _ in range(4)]
dxdy = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))

for _ in range(M):
    x, y, d = map(lambda x: int(x)-1, input().split())
    arr[x][y][d]+=1

die = [[-1]*4 for _ in range(4)]

for t in range(T):

    tmp = [[ele[:] for ele in row] for row in arr]
    arr = [[[0]*8 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for d in range(8):
                if tmp[i][j][d]==0: continue
                nd = d
                for _ in range(8):
                    dx, dy = dxdy[nd]
                    nx, ny = i+dx, j+dy
                    if not(0<=nx<4 and 0<=ny<4) or (nx, ny)==(px, py) or die[nx][ny]>=t:
                        nd = (nd+1)%8
                        continue
                    arr[nx][ny][nd]+=tmp[i][j][d]
                    break
                else:
                    arr[i][j][d]+=tmp[i][j][d]

    mcnt = -1
    root = []
    btk(0, [])

    px, py = root[-1]
    for x, y in root:
        if sum(arr[x][y])!=0:
            die[x][y] = t+2
        arr[x][y] = [0]*8
    x
    for i in range(4):
        for j in range(4):
            for d in range(8):
                arr[i][j][d]+=tmp[i][j][d]
    x


print(sum([sum([sum(ele) for ele in row]) for row in arr]))