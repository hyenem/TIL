from collections import deque


def rotate(idx):
    tmp = [ele[:] for ele in maze[idx]]
    for i in range(5):
        for j in range(5):
            maze[idx][i][j]=tmp[4-j][i]

def compute():

    global ans
    if not maze[0][0][0]: return

    if ans==12: return

    visited = [[[0]*5 for _ in range(5)] for _ in range(5)]
    q = deque([(0, 0, 0, 0)])
    visited[0][0][0]=1
    while q:
        cnt, x, y, z = q.popleft()
        if cnt>=ans: return
        if x==y==z==4:
            ans = min(ans, cnt)
            break
        for dx, dy, dz in dxdydz:
            nx, ny, nz = x+dx, y+dy, z+dz
            if not(0<=nx<5 and 0<=ny<5 and 0<=nz<5): continue
            if visited[nx][ny][nz]: continue
            if not maze[nx][ny][nz]: continue
            visited[nx][ny][nz]=1
            q.append((cnt+1, nx, ny, nz))

def solution(idx):

    if ans==12 : return

    if idx==5:
        compute()
        return

    solution(idx+1)
    for _ in range(3):
        rotate(idx)
        solution(idx+1)

def combination():
    if ans==12: return

    if len(comb)==5:
        maze.clear()
        for i in comb:
            maze.append([ele[:] for ele in mazelevel[i]])
        solution(0)
        return
    for i in range(5):
        if i not in comb:
            comb.append(i)
            combination()
            comb.pop()

maze = []
mazelevel = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
dxdydz = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
ans = 126
comb = []
combination()
if ans==126:
    ans = -1
print(ans)