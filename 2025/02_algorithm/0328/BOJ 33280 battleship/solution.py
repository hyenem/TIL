import sys
sys.setrecursionlimit(10**5)

def dfs(x, y):
    cnt = 0
    for d in range(4):
        dx, dy = dxdy[d]
        nx, ny = x+dx, y+dy
        if not(0<=nx<N and 0<=ny<M) or arr[nx][ny]=='#': continue
        while (0<=nx+dx<N and 0<=ny+dy<M) and not arr[nx+dx][ny+dy]=='#':
            nx, ny = nx+dx, ny+dy

        arr[nx][ny]='#'
        tmpcnt = dfs(nx, ny)

        if tmpcnt==0: continue
        cnt += tmpcnt
        ans.append((x+1, y+1, tmpcnt, dict[d]))

    return cnt+1


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
K = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]=='.':
            K += 1
x, y = map(int, input().split())
arr[x-1][y-1] = '#'
ans = []
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
dict = ['U', 'R', 'D', 'L']

dfs(x-1, y-1)

if len(ans)==K-1:
    print('YES')
    print(K-1)
    for ele in ans[::-1]:
        print(*ele)
else:
    print('NO')