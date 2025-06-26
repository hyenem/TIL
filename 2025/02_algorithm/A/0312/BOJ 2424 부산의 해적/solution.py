N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dxdy = ((1, 0), (-1, 0), (0, 1), (0, -1))
enemy = []
me = []
ervisited = [[0]*M for _ in range(N)]
mvisited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]=='Y':
            me.append((i,j))
            mvisited[i][j]=1
        elif arr[i][j]=='V':
            enemy.append((i,j))
            ervisited[i][j]=1
        elif arr[i][j]=='T':
            goal = (i,j)

ans = 0
evisited= [[[0, 0] for _ in range(M)] for _ in range(N)]
nenemy = []
while enemy:
    ex, ey = enemy.pop()

    for dx, dy in dxdy:
        nx, ny = ex + dx, ey + dy
        if not (0 <= nx < N and 0 <= ny < M): continue
        if ervisited[nx][ny]: continue
        if arr[nx][ny] == 'I': continue
        nenemy.append((nx, ny))
        ervisited[nx][ny]=1

    for d in range(4):
        dx, dy = dxdy[d]
        nx, ny = ex, ey
        while True:
            nx, ny = nx + dx, ny + dy
            if not (0 <= nx < N and 0 <= ny < M): break
            if evisited[nx][ny][d // 2]: break
            if arr[nx][ny] == 'I': break
            arr[nx][ny] = 'V'
            evisited[nx][ny][d // 2] = 1

    evisited[ex][ey][0], evisited[ex][ey][1] = 1, 1
enemy = nenemy

while me :
    nenemy = []
    nme = []

    while enemy:
        ex, ey = enemy.pop()

        for dx, dy in dxdy:
            nx, ny = ex+dx, ey+dy
            if not(0<=nx<N and 0<=ny<M): continue
            if ervisited[nx][ny]: continue
            if arr[nx][ny]=='I': continue
            nenemy.append((nx, ny))
            ervisited[nx][ny]=1

        for d in range(4):
            dx, dy = dxdy[d]
            nx, ny = ex, ey
            while True:
                nx, ny = nx+dx, ny+dy
                if not (0 <= nx < N and 0 <= ny < M): break
                if evisited[nx][ny][d//2]: break
                if arr[nx][ny] == 'I': break
                arr[nx][ny]='V'
                evisited[nx][ny][d//2]=1

        evisited[ex][ey][0], evisited[ex][ey][1]=1, 1
    enemy = nenemy

    while me:
        mx, my = me.pop()
        for dx, dy in dxdy:
            nx, ny = mx+dx, my+dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            if mvisited[nx][ny]: continue
            if arr[nx][ny] in {'I', 'V'}: continue
            if (nx, ny)==goal:
                ans = 1
                break
            nme.append((nx, ny))
            mvisited[nx][ny]=1
        if ans: break
    if ans : break
    me = nme


if ans: print('YES')
else : print('NO')