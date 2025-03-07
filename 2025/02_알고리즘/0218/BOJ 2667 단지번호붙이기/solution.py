from collections import deque

N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
dxdy = ((1, 0), (-1, 0), (0, 1), (0, -1))

ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            q = deque()
            q.append((i, j))
            arr[i][j]=0
            cnt = 0
            while q:
                x, y = q.popleft()
                cnt+=1
                for dx, dy in dxdy:
                    nx, ny = x+dx, y+dy
                    if not(0<=nx<N and 0<=ny<N): continue
                    if arr[nx][ny]==1:
                        arr[nx][ny]=0
                        q.append((nx, ny))
            ans.append(cnt)
ans.sort()
print(len(ans))
for ele in ans:
    print(ele)