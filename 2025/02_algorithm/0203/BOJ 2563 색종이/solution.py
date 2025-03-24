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
            ans += 1
print(ans)