from collections import deque
def pm(x, y):
    pmx = 0 if x>=0 else 1
    pmy = 0 if y>=0 else 1
    return pmx+2*pmy

sx, sy =map(int, input().split())
gx, gy =map(int, input().split())
N = int(input())
cmds = list(map(int, input().split()))
T = max(cmds)

N = 500
visited = [[[[0, 0, 0, 0] for _ in range(4)] for _ in range(N+1)] for _ in range(N+1)]
q = deque([(sx, sy, 0)])
k=pm(sx, sy)
visited[abs(sx)][abs(sy)][k][0]=1
ans = [-1, -1, -1, -1]

while q:
    x, y, cnt = q.popleft()
    if cnt>T:
        break

    if (x, y)==(gx, gy) and ans[cnt%4]==-1:
        ans[cnt%4]=cnt
        if ans.count(-1)==0: break

    for nx, ny in ((x+1, y), (2*x, 2*y), (-y, x)):
        if abs(nx)>N or abs(ny)>N: continue
        k = pm(nx, ny)
        if visited[abs(nx)][abs(ny)][k][(cnt+1)%4]: continue
        visited[abs(nx)][abs(ny)][k][(cnt+1)%4]=1
        q.append((nx, ny, cnt+1))

for c in cmds:
    if 0<=ans[c%4]<=c:
        print('YES')
    else:
        print('NO')