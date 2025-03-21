from collections import deque

N, M = map(int, input().split())
L, R = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]==2:
            q = deque([(i, j, L, R)])
            arr[i][j]=1
            up = i
            while up-1>=0 and arr[up-1][j]!=1:
                up -= 1
                q.append((up, j, L, R))
                arr[up][j]=1
            down = i
            while down+1<N and arr[down+1][j]!=1:
                down+=1
                q.append((down, j, L, R))
                arr[down][j]=1
            break

ans = 0
while q:
    x, y, l, r = q.popleft()
    ans += 1

    if r != 0 and y+1<M and arr[x][y+1]==0:
        ny = y+1
        q.append((x, ny, l, r-1))
        arr[x][ny] = 1
        up = x
        while up - 1 >= 0 and arr[up - 1][ny] != 1:
            up -= 1
            q.append((up, ny, l, r-1))
            arr[up][ny] = 1
        down = x
        while down + 1 < N and arr[down + 1][ny] != 1:
            down += 1
            q.append((down, ny, l, r-1))
            arr[down][ny] = 1

    if l != 0 and y-1>=0 and arr[x][y-1]==0:
        ny = y-1
        q.append((x, ny, l-1, r))
        arr[x][ny] = 1
        up = x
        while up - 1 >= 0 and arr[up - 1][ny] != 1:
            up -= 1
            q.append((up, ny, l-1, r))
            arr[up][ny] = 1
        down = x
        while down + 1 < N and arr[down + 1][ny] != 1:
            down += 1
            q.append((down, ny, l-1, r))
            arr[down][ny] = 1

print(ans)