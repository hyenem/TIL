N = int(input())
visited = [[False]*101 for _ in range(101)]
ans = 0
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if visited[i][j]:
                continue
            visited[i][j]=True
dx=(-1, 1, 0, 0)
dy=(0, 0, -1, 1)
for i in range(101):
    for j in range(101):
        if visited[i][j]:
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                #가장자리인 경우 둘레 1 증가
                if (not 0<=nx<101) or (not 1<= ny <101) or not visited[nx][ny]:
                    ans += 1
print(ans)