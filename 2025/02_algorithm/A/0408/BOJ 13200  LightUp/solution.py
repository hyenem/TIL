def cbtk(idx, candidate):
    global visited, ans, light
    if idx==len(candidate):
        for i in range(N):
            for j in range(N):
                if arr[i][j] == -2 and not light[i][j]:
                    return False
        return True


    if cbtk(idx+1, candidate):
        return True

    x, y = candidate[idx]
    if not light[x][y] and not visited[x][y]:
        tvisited = [ele[:] for ele in visited]
        tlight = [ele[:] for ele in light]
        tans = [ele[:] for ele in ans]

        lightup(x, y)
        if cbtk(idx+1, candidate):
            return True
        visited = [ele[:] for ele in tvisited]
        light = [ele[:] for ele in tlight]
        ans = [ele[:] for ele in tans]

def check():
    candidate = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] or light[i][j]: continue
            candidate.append((i, j))

    return cbtk(0, candidate)

def lightup(x, y):
    ans[x][y]=1
    visited[x][y]=1
    light[x][y]=1
    for dx, dy in dxdy:
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<N:
            visited[nx][ny]=1

    for dx, dy in dxdy:
        nx, ny = x, y
        while 0<=nx+dx<N and 0<=ny+dy<N and arr[nx+dx][ny+dy]==-2:
            nx, ny = nx+dx, ny+dy
            light[nx][ny]=1

def btk(idx):
    global visited, light, ans

    if idx == len(numblack):
        return check()

    bx, by = numblack[idx]
    num = arr[bx][by]
    tvisited = [ele[:] for ele in visited]
    tlight = [ele[:] for ele in light]
    tans = [ele[:] for ele in ans]
    for dirs in direction[num]:
        for d in range(4):
            dx, dy =dxdy[d]
            nx, ny = bx+dx, by+dy
            if d in dirs:
                if not(0<=nx<N and 0<=ny<N) or ((visited[nx][ny] or light[nx][ny]) and not ans[nx][ny]):
                    break
            else:
                if 0<=nx<N and 0<=ny<N and ans[nx][ny]:
                    break
        else:
            for d in range(4):
                dx, dy = dxdy[d]
                nx, ny = bx + dx, by + dy
                if d in dirs:
                    lightup(nx, ny)
                elif 0<=nx<N and 0<=ny<N:
                    visited[nx][ny]=1
            if btk(idx+1): return True

            visited = [ele[:] for ele in tvisited]
            light = [ele[:] for ele in tlight]
            ans = [ele[:] for ele in tans]
    return False

T = int(input())
direction = [0, ((0,), (1, ), (2, ), (3,)), ((0,1), (0,2), (0,3), (1, 2), (1, 3), (2, 3)), ((0, 1, 2), (0, 1, 3),(0, 2, 3), (1, 2, 3)), ((0, 1, 2, 3),)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    light = [[0]*N for _ in range(N)]
    ans = [[0]*N for _ in range(N)]

    numblack = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]==-2: continue
            visited[i][j]=1
            if arr[i][j]==0:
                for dx, dy in dxdy:
                    nx, ny= i+dx, j+dy
                    if not (0<=nx<N and 0<=ny<N): continue
                    visited[nx][ny]=1
            elif arr[i][j]>=1:
                numblack.append((i, j))

    btk(0)
    for ele in ans:
        print(*ele)