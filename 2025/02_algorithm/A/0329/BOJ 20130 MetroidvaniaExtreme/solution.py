from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

item = set()
q = deque()
ans = []
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j]=='@':
            q.append((i, j))
            visited[i][j]=1
            arr[i][j]='*'
            break
    if len(q)!=0:
        break

while q:
    x, y = q.popleft()

    if 0<=ord(arr[x][y])-ord('A')<26 and ord(arr[x][y])-ord('A') not in item:
        q.append((x, y))
        continue

    ans.append((x+1, y+1))
    if 0<=ord(arr[x][y])-ord('a')<26:
        item.add(ord(arr[x][y])-ord('a'))
    if arr[x][y]=='!':
        break

    for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nx, ny = x+dx, y+dy
        if arr[nx][ny]=='#' or visited[nx][ny]: continue

        visited[nx][ny]=1
        q.append((nx, ny))

print(len(ans))
for ele in ans:
    print(*ele)