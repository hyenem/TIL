'''
5 10
4 4 4
0 0 0
4 2 3
2 4 4
3 3 3
1 1 1
2 2 2
2 1 3
3 4 0
0 2 1
0 1 2

* 사람은 윗면의 0, 0에서 시작한다고 하는게 어떨까?
'''
def move(x, y, z, d):
    dx, dy = ((-1, 0), (0, 1), (1, 0), (0, -1))[d]
    nx, ny = x+dx, y+dy
    if 0<=nx<N and 0<=ny<N:
        return nx, ny, z

    if z==4:
        nx, nz = 0, d
        ny = (N-1-y, x, y, N-1-x)[d]
    elif z==5:
        nx, nz = N-1, (d+2)%4
        ny = (y, x, N-1-y, N-1-x)[d]
    else :

        if d==0:
            nz = 4
            nx, ny = ((0, N-1-y), (N-1-y, N-1), (N-1, y), (y, 0))[z]
        elif d==2:
            nz = 5
            nx, ny = ((N-1, N-1-y), (y, N-1), (0, y), (N-1-y, 0))[z]
        else :
            nx, nz = x, (z+d)%4
            ny = 0 if d==1 else N-1

    return nx, ny, nz


N, M = map(int,input().split())     # 정육면체 사이즈, 주어지는 불 좌표 개수
goal = tuple(map(int, input().split()))  # 목적 출구
x, y, z = 0, 0, 4
fire = [tuple(map(int, input().split())) for _ in range(M)]
person = [(x, y, z)]

surface = [[[0]*N for _ in range(N)] for _ in range(6)]
cube = [[[0]*N for _ in range(N)] for _ in range(N)]
surface[z][x][y]=1
for x, y, z in fire:
    cube[x][y][z]=1
    if x == 0:
        surface[2][z][y] = 2
    elif x == N - 1:
        surface[0][z][N - 1 - y] = 2
    if y == 0:
        surface[3][z][x] = 2
    elif y == N - 1:
        surface[1][z][N - 1 - x] = 2
    if z == 0:
        surface[4][x][y] = 2
    elif z == N - 1:
        surface[5][N - 1 - x][N - 1 - y] = 2

time = 0
ans = -1
while person:
    nperson = []
    nfire = []

    while fire:
        fx, fy, fz = fire.pop()
        for dx, dy, dz in ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
            nx, ny, nz = fx+dx, fy+dy, fz+dz
            if not(0<=nx<N and 0<=ny<N and 0<=nz<N): continue
            if cube[nx][ny][nz]: continue
            cube[nx][ny][nz]=1
            nfire.append((nx, ny, nz))

            if nx==0:       surface[2][nz][ny]=2
            elif nx==N-1:   surface[0][nz][N-1-ny]=2
            if ny==0:       surface[3][nz][nx]=2
            elif ny==N-1:   surface[1][nz][N-1-nx]=2
            if nz==0:       surface[4][nx][ny]=2
            elif nz==N-1:   surface[5][N-1-nx][N-1-ny]=2
    fire = nfire

    while person:
        px, py, pz = person.pop()
        if (px, py, pz)==goal:
            ans = time
            break

        for d in range(4):
            nx, ny, nz = move(px, py, pz, d)
            if surface[nz][nx][ny]: continue
            surface[nz][nx][ny]=1
            nperson.append((nx, ny, nz))
    else:
        time += 1
        person = nperson
        continue
    break

print(ans)