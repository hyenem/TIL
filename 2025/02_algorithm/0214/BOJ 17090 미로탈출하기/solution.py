N, M = map(int, input().split())
dxdy = {'D':(1, 0), 'U':(-1, 0), 'L':(0,-1), 'R':(0,1)}
arr = [list(input()) for _ in range(N)]
# visited의 0은 아직 안본길, 1은 바깥으로 연결된길
# -1은 바깥으로 연결 안된 길, 2는 지금 가고있는 길입니다.
visited = [[0]*M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]!=0: continue
        x, y= i,j
        stack = []
        stack.append((x, y))
        acc = 0
        flag = False
        while True:
            acc+=1
            visited[x][y]=2
            dx, dy = dxdy[arr[x][y]]
            x, y = x+dx, y+dy
            if not(0<=x<N and 0<=y<M):
                flag = True
                ans += acc
                break
            # 처음엔 이걸 스택에 있는지 없는지로 해서
            # 시간초과 났습니다.
            if visited[x][y]==2:
                break
            if visited[x][y]==1:
                flag = True
                ans += acc
                break
            if visited[x][y]==-1:
                break
            stack.append((x,y))
        if flag:
            while stack:
                x, y = stack.pop()
                visited[x][y]=1
        else :
            while stack:
                x, y = stack.pop()
                visited[x][y]=-1


print(ans)
