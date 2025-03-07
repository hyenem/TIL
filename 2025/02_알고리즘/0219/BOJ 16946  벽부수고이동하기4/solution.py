dxdy = ((1, 0), (-1, 0), (0, 1), (0, -1))

N, M = map(int, input().split())
arr = [list(map(int,input())) for _ in range(N)]
cal = [[(0,0)]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]==0 and cal[i][j][1]==0:
            cnt+=1
            q = [(i, j)]
            visited[i][j]=True
            idx = 0
            while idx<len(q):
                x, y = q[idx]
                idx+=1
                for dx, dy in dxdy:
                    nx, ny = x+dx, y+dy
                    if not(0<=nx<N and 0<=ny<M): continue
                    if visited[nx][ny]:continue
                    if arr[nx][ny]==1: continue
                    visited[nx][ny]=True
                    q.append((nx, ny))
            for x, y in q:
                cal[x][y]=(cnt, len(q))
for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            s = set()
            for dx, dy in dxdy:
                nx, ny = i+dx, j+dy
                if not(0<=nx<N and 0<=ny<M): continue
                if arr[nx][ny]==1: continue
                print(nx, ny)
                if cal[nx][ny][0] in s: continue
                s.add(cal[nx][ny][0])
                arr[i][j]+=cal[nx][ny][1]
for ele in arr:
    print(''.join(map(lambda x: str(x%10), ele)))