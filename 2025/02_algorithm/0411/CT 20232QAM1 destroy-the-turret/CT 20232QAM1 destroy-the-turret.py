from collections import deque

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
attack_time = [[-1]*M for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0))

for turn in range(K):

    attack = (-1000000000, 0, 0, 0)
    defence = (0, 0, 0, 0)
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0: continue

            this = (-arr[i][j], attack_time[i][j], i+j, j)
            attack = max(attack, this)
            defence = min(defence, this)

    ax, ay = attack[2]-attack[3], attack[3]
    dfx, dfy = defence[2]-defence[3], defence[3]
    if (ax, ay)==(dfx, dfy):
        break

    visited[ax][ay]=turn
    visited[dfx][dfy]=turn
    arr[ax][ay]+=N+M
    attack_time[ax][ay]=turn

    q = deque([(ax, ay, [])])
    qvisited = [[0]*M for _ in range(N)]
    qvisited[ax][ay]=1
    while q:
        x, y, root = q.popleft()
        if (x, y)==(dfx, dfy):
            arr[x][y]=max(0, arr[x][y]-arr[ax][ay])
            root.pop()
            for nx, ny in root:
                arr[nx][ny] = max(0, arr[nx][ny]-arr[ax][ay]//2)
                visited[nx][ny]=turn
            break

        for dx, dy in dxdy:
            nx, ny = (x+dx)%N, (y+dy)%M
            if qvisited[nx][ny]: continue
            if arr[nx][ny]==0: continue
            qvisited[nx][ny]=1
            q.append((nx, ny, root+[(nx, ny)]))
    else:
        arr[dfx][dfy] = max(0, arr[dfx][dfy] - arr[ax][ay])
        for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)):
            nx, ny = (dfx+dx)%N, (dfy+dy)%M
            if arr[nx][ny]==0: continue
            if (nx, ny)==(ax, ay): continue
            arr[nx][ny]-=arr[ax][ay]//2
            visited[nx][ny]=turn

    arr
    for i in range(N):
        for j in range(M):
            if visited[i][j]==turn: continue
            if arr[i][j]==0: continue
            arr[i][j]+=1
    arr


print(max(map(max, arr)))