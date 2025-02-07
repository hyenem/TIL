from collections import deque

N, M = map(int, input().split())
visited=[[False]*(M) for _ in range(N)]
K = int(input())
for _ in range(K):
    br, bc = map(int, input().split())
    visited[br][bc]=True

x, y = map(int, input().split())
visited[x][y]=True

direction = [(0,0), (-1, 0),(1,0),(0,-1),(0,1)]
dxdy = list(map(lambda x: direction[int(x)], input().split()))

move = True
while move:
    move = False
    for dx, dy in dxdy:
        while True:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                visited[nx][ny]=True
                x, y = nx, ny
                move = True
            else :
                break
print(x, y)
