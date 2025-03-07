import sys
sys.setrecursionlimit(100000)

def dfs(i, j):
    if DP[i][j]==-1:
        res = 0
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = i+dx, j+dy
            if not (0<=nx<N and 0<=ny<M): continue
            if arr[nx][ny]>arr[i][j]:
                res += dfs(nx, ny)
        DP[i][j]=res
        if res>100000000:
            print(0)
            exit()
    return DP[i][j]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[-1]*M for _ in range(N)]
DP[0][0]=1

print(dfs(N-1, M-1))