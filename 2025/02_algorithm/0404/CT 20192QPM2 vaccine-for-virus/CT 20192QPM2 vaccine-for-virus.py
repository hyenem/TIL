'''2회독
제출횟수 : 1회
풀이시간 : 13분

* 예제에 바이러스 하나도 없는거 줘서 망정이지
* 초기조건 항상 채크해야합니다~~~~~
'''

from collections import deque

def bfs():
    q = deque()
    visited = [[0]*N for _ in range(N)]
    for i, j in choice:
        visited[i][j]=1
        q.append((0, i, j))

    cnt = 0
    while q:
        t, x, y = q.popleft()
        if arr[x][y]==0:
            cnt+=1
        if cnt==virus:
            return t
        for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<N): continue
            if visited[nx][ny] or arr[nx][ny]==1: continue

            visited[nx][ny]=1
            q.append((t+1, nx, ny))

    return N*N+1



def btk(idx):
    global ans
    if len(choice)==M:
        ans = min(ans, bfs())
        return

    for i in range(idx, len(hospital)):
        choice.append(hospital[i])
        btk(i+1)
        choice.pop()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

hospital = []
virus = 0

for i in range(N):
    for j in range(N):
        if arr[i][j]==0:
            virus += 1
        elif arr[i][j]==2:
            hospital.append((i, j))

ans = N*N+1
choice = []
btk(0)
if ans==N*N+1: ans = -1
print(ans)