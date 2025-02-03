import sys
sys.getrecursionlimit(10000)

dx=(-1, 1, 0, 0)
dy=(0, 0, -1, 1)

def dfs(i, j):
    global cnt
    for k in range(4):
        ni = i+dx[k]
        nj = j+dy[k]
        if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
            cnt +=1
            visited[ni][nj]=True
            dfs(ni, nj)

N, M, K = map(int, input().split())
visited = [[False]*(M) for _ in range(N)]
ans = []
for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            # 색칠한 되는 방문표시
            visited[i][j]=True

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            #cnt는 1이고 dfs한 번 돌떄마다 1씩 증가(즉 넓이를 의미)
            cnt = 1
            visited[i][j]=True
            dfs(i, j)
            ans.append(cnt)
ans.sort()
print(len(ans))
print(*ans)