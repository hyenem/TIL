def color_visited(ux, uy, u):
    visited_r[ux][u] = 1
    visited_c[uy][u] = 1
    visited_b[(ux // 3) * 3 + uy // 3][u] = 1

def delete_visited(ux, uy, u):
    visited_r[ux][u] = 0
    visited_c[uy][u] = 0
    visited_b[(ux // 3) * 3 + uy // 3][u] = 0

def check_visited(ux, uy, u):
    if visited_r[ux][u] or visited_c[uy][u] or visited_b[(ux // 3) * 3 + uy // 3][u]:
        return False
    return True

def btk(cnt, idx):
    if cnt==36-N:
        return True
    if idx==81:
        return False

    x, y = idx//9, idx%9
    if arr[x][y]!=0:
        return btk(cnt, idx+1)

    for i in range(1,10):
        if not check_visited(x, y, i):
            continue
        color_visited(x, y, i)
        arr[x][y]=i
        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if not(0<=nx<9 and 0<=ny<9) or arr[nx][ny]!=0: continue
            for j in range(1, 10):
                if i==j or visited[i][j]: continue
                if not check_visited(nx, ny, j): continue
                color_visited(nx, ny, j)
                arr[nx][ny]=j
                visited[i][j]=1
                visited[j][i]=1
                if btk(cnt+1, idx+1):
                    return True
                arr[nx][ny]=0
                visited[i][j]=0
                visited[j][i]=0
                delete_visited(nx, ny, j)
        arr[x][y]=0
        delete_visited(x, y, i)
    return False

tc = 0
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
while True:
    tc+=1
    N = int(input())
    if N==0: break

    visited = [[0]*10 for _ in range(10)]
    arr = [[0]*9 for _ in range(9)]

    visited_r = [[0]*10 for _ in range(9)]
    visited_c = [[0]*10 for _ in range(9)]
    visited_b = [[0]*10 for _ in range(9)]

    for _ in range(N):
        u, lu, v, lv = input().split()
        u, v = int(u), int(v)
        ux, uy = ord(lu[0])-ord('A'), int(lu[1])-1
        vx, vy = ord(lv[0])-ord('A'), int(lv[1])-1
        color_visited(ux, uy, u)
        color_visited(vx, vy, v)
        visited[u][v] = 1
        visited[v][u] = 1
        arr[ux][uy]=u
        arr[vx][vy]=v

    data = list(input().split())
    for n in range(1,10):
        l = data[n-1]
        x, y = ord(l[0]) - ord('A'), int(l[1]) - 1
        arr[x][y]=n
        color_visited(x, y, n)

    btk(0, 0)
    print(f'Puzzle {tc}')
    for ele in arr:
        print(''.join(map(str, ele)))
