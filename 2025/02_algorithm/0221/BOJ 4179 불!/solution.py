from collections import deque

def bfs():
    global q, fire
    ans = 0

    while q:
        ans += 1
        newfire = deque()
        while fire:
            x, y = fire.pop()
            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < N and 0<=ny<M): continue
                if arr[nx][ny] in {'#', 'F'}: continue
                arr[nx][ny]='F'
                newfire.append((nx,ny))
        fire = newfire

        newq = deque()
        while q:
            x, y = q.popleft()
            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < N and 0<=ny<M):
                    return ans
                if arr[nx][ny] in {'#', 'F'} or visited[nx][ny]: continue
                visited[nx][ny]=True
                newq.append((nx, ny))
        q = newq

    return -1

dxdy = ((1, 0), (-1, 0), (0, 1), (0,-1))
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

ans = N*M
q = deque()
fire = []
visited = [[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]=='F':
            fire.append((i,j))
        elif arr[i][j]=='J':
            q.append((i,j))
            visited[i][j]=True

ans = bfs()
if ans==-1:
    print('IMPOSSIBLE')
else : print(ans)