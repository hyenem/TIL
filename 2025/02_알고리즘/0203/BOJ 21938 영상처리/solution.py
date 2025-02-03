import sys
sys.setrecursionlimit(10000)

dx=(-1, 1, 0, 0)
dy = (0, 0, -1, 1)
def dfs(i, j):
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
            visited[ni][nj]=True
            dfs(ni, nj)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
T = int(input())
visited = [[True]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        avg = (arr[i][j*3]+arr[i][j*3+1]+arr[i][j*3+2])//3
        if avg>=T:
            visited[i][j]=False

cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            cnt += 1
            visited[i][j] = True
            dfs(i, j)
print(cnt)