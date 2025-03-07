from collections import deque

def bfs():
    global ans
    while q:
        time, x, y = q.popleft()
        if ans!=-1 and time>=ans: return
        if y+time+1>500000: continue
        visited[x][time%2]=True
        ny = y+time+1
        if visited[ny][(time+1)%2]:
            ans = time+1
        for nx in {x-1, x+1, 2*x}:
            if nx<0 or nx>500000: continue
            if nx==ny:
                ans = time+1
                return
            if visited[nx][(time+1)%2]:continue
            visited[nx][(time+1)%2]=True
            q.append((time+1, nx, ny))


N, K = map(int, input().split())
visited=[[False, False] for _ in range(500001)]
if N==K:
    print(0)
else :
    q = deque()
    q.append((0, N, K))
    ans = -1
    bfs()
    print(ans)