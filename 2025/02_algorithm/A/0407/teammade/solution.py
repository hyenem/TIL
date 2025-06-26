def move(x, y, z, d):
    dx, dy = dxdy[d]
    nx, ny = x+dx, y+dy
    if 0<=nx<N and 0<=ny<N:
        return nx, ny, z

    if z==4:
        nx, nz = 0, d
        ny = (x, y, N-1-x, N-1-y)[d]
    elif z==5:
        nx, nz = 0, (d+2)%4
        ny = (N-1-x, N-1-y, x, y)[d]
    else:
        if d==3:
            nz = 4
            nx, ny = ((y, 0), (N-1, y), (N-1-y, N-1), (0, N-1-y))[z]
        elif d==1:
            nz = 5
            nx, ny = ((N-1-y, 0), (0, y), (y, N-1), (N-1, N-1-y))[z]
        else:
            nx, nz = x, (z+(d-1))%4
            ny = 0 if d==2 else N-1
    return nx, ny, nz

N, K = map(int, input().split())

surface = [0]*6
cube = [[[0]*N for _ in range(N)] for _ in range(N)]
switch = (4, 0, 1, 2, 3, 5)
for i in range(6):
    s = [list(map(int, input().split())) for _ in range(N)]
    surface[switch[i]] = s

for s in range(6):
    for i in range(N):
        for j in range(N):
            if surface[s][i][j]==3:
                sx, sy, sz = i, j, s
            elif surface[s][i][j]==4:
                goal = (i, j, s)

dxdy = ((0, -1), (1, 0), (0, 1), (-1, 0))
fire = [tuple(map(int, input().split())) for _ in range(K)]
for x, y, z in fire:
    cube[x][y][z]=1
    if x==0: surface[2][N-1-z][N-1-y]=1
    elif x==N-1: surface[0][N-1-z][y]=1
    if y==0: surface[3][N-1-z][x]=1
    elif y==N-1: surface[1][N-1-z][N-1-x]=1
    if z==0: surface[5][N-1-y][x]=1
    elif z==N-1: surface[4][y][N-1-x]=1

people = [(sx, sy, sz)]
time = 0
while people:

    npeople = []
    for x, y, z in people:
        if (x, y, z) == goal:
            print(time)
            break
        for d in range(4):
            nx, ny, nz = move(x, y, z, d)
            if surface[nz][nx][ny] not in {0, 4}: continue
            surface[nz][nx][ny] = 1
            npeople.append((nx, ny, nz))
    else:
        people = npeople

        if time != 0 and time % 3 == 0:
            nfire = []
            for x, y, z in fire:
                for dx, dy, dz in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
                    nx, ny, nz = x + dx, y + dy, z + dz
                    if not (0 <= nx < N and 0 <= ny < N and 0 <= nz < N): continue
                    if cube[nx][ny][nz]: continue
                    nfire.append((nx, ny, nz))
                    cube[nx][ny][nz] = 1
                    if nx == 0:
                        surface[2][N - 1 - nz][N - 1 - ny] = 1
                    elif nx == N - 1:
                        surface[0][N - 1 - nz][ny] = 1
                    if ny == 0:
                        surface[3][N - 1 - nz][nx] = 1
                    elif ny == N - 1:
                        surface[1][N - 1 - nz][N - 1 - nx] = 1
                    if nz == 0:
                        surface[5][N - 1 - ny][nx] = 1
                    elif nz == N - 1:
                        surface[4][ny][N - 1 - nx] = 1
            fire = nfire

        time += 1
        continue

    break
else:
    print(-1)

'''
4 3
3 0 1 0
0 0 0 0
1 0 1 0
0 0 0 0
0 0 0 0
0 1 1 0
0 0 0 0
0 0 0 0
0 0 0 0
1 0 1 0
0 0 0 0
0 1 0 0
0 0 0 0
0 0 4 0
0 1 0 0
0 0 0 1
0 0 0 0
0 0 0 0
1 1 0 0
0 0 0 0
0 0 0 0
0 1 0 0
0 0 0 0
0 0 0 0
1 2 3
3 0 0
2 2 1

'''