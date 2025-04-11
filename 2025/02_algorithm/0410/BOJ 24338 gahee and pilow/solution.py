from collections import deque

increase = {'W': 3, 'E':1, 'N':0, 'S':2}
increase2 = ('N', 'E', 'S', 'W')
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
gx, gy = map(lambda x:int(x)-1, input().split())

visited = [[0] * M for _ in range(N)]
q = deque([(gx, gy, 0, [])])
visited[gx][gy] = 1

while q:
    x, y, d, root = q.popleft()
    if arr[x][y] in {'B', 'P'}:
        for x, y, d in root:
            arr[x][y]=d

        for row in arr:
            ans = ''
            for ele in row:
                if ele=='?':
                    ans+='N'
                else: ans += ele
            print(ans)
        break

    if root and (root[-1][0], root[-1][1])==(x, y):
        dx, dy = dxdy[d]
        nx, ny = x+dx, y+dy
        if not(0<=nx<N and 0<=ny<M): continue
        if visited[nx][ny]: continue

        if d==increase[root[-1][2]]:
            if arr[nx][ny]=='1':
                visited[nx][ny]=1
                q.append((nx, ny, d, root))
        else:
            if arr[nx][ny] in {'.', 'B', 'P'}:
                visited[nx][ny]=1
                q.append((nx, ny, d, root))

    else:
        for d in range(4):
            dx, dy = dxdy[d]
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            if visited[nx][ny]: continue
            if arr[nx][ny]=='#': continue
            if arr[x][y]=='1' and arr[nx][ny] in {'.', 'B', 'P'}: continue
            if arr[x][y]!='1' and arr[nx][ny]=='1': continue

            if arr[nx][ny]=='?':
                for rx, ry, rd in root:
                    if (nx, ny)==(rx, ry):
                        break
                else:
                    if arr[x][y]=='1':
                        q.append((nx, ny, d, root+[(nx, ny, increase2[(d+2)%4])]))
                    else:
                        q.append((nx, ny, d, root+[(nx, ny, increase2[d])]))
            else:
                visited[nx][ny]=1
                q.append((nx, ny, d, root))

else:
    print(-1)