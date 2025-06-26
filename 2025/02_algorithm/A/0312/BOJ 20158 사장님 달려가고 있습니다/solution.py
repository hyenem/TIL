from collections import deque

N = int(input())
arr= [list(map(int, input().split())) for _ in range(N)]
visited = [[[set(), set(), set(), set()] for _ in range(N)] for _ in range(N)]
dxdy = ((1, 0), (0, 1), (-1, 0), (0, -1))

if N==1:
    print(0)
else :
    q = deque()
    if arr[0][1]!=1:
        q.append((1, 1, 1, 0, 1))
        visited[0][0][1].add(1)
    if arr[1][0]!=1:
        q.append((1, 1, 0, 1, 0))
        visited[0][0][0].add(1)

    while q:
        t, acc, d, x, y = q.popleft()
        if x==y==N-1:
            print(t)
            break

        for nd in range(4):
            dx, dy = dxdy[nd]
            if d==nd:
                if acc+1 in visited[x][y][d]: continue
                visited[x][y][d].add(acc+1)
                nx, ny = x + dx*(acc+1), y + dy*(acc+1)
                if not (0 <= nx < N and 0 <= ny < N): continue
                if arr[nx][ny] != 0 and arr[nx][ny] <= t + 1: continue

                for k in range(1, acc+1):
                    nx, ny = x+dx*k, y+dy*k

                    if not(0<=nx<N and 0<=ny<N): break
                    if arr[nx][ny]!=0 and arr[nx][ny]<t+1:
                        break
                else :
                    q.append((t+1, acc+1, d, nx+dx, ny+dy))

            else :
                if 1 in visited[x][y][nd]: continue

                visited[x][y][nd].add(1)
                nx, ny = x+dx, y+dy
                if not (0 <= nx < N and 0 <= ny < N): continue
                if arr[nx][ny] != 0 and arr[nx][ny] <= t+1: continue
                q.append((t+1, 1, nd, nx, ny))

    else:
        print('Fired')