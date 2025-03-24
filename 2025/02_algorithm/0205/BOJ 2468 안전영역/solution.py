N = int(input())
arr= [list(map(int, input().split())) for _ in range(N)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 죄다 1인 경우,, 어떻게 되는건지 모르겠음,,,
# 비의 높이가 0일수도 있는지,,,
ans = 1
for h in range(1, 100):
    visited =[[False]*N for _ in range(N)]
    cnt = 0
    q = []
    for i in range(N):
        for j in range(N):
            # 비보다 높은 땅중 방문 안한 땅 깔때마다
            if arr[i][j]>h and not visited[i][j]:
                # cnt 1씩 올려주고
                cnt+=1
                # 그 땅이랑 연결된 땅 다 방문표시
                q.append((i, j))
                visited[i][j]=True
                while q:
                    x, y = q.pop(0)
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0<=nx<N and 0<=ny<N and arr[nx][ny]>h and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
    ans = max(ans, cnt)
    # 모두다 비에 잠기면 더이상 안해도 됨
    if cnt == 0:
        break
print(ans)