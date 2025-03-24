N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dxdy = ((1, 0), (-1, 0), (0, 1), (0, -1))

ans = []
for i in range(N):
    for j in range(M):
        # 처음에 방문한 곳은 보지 않아서 고전했음
        # 방문해도 봐야만함(거기가 중심일수도 있기 때문)
        if arr[i][j]=='.': continue
        # *을 기준으로 사방이 다 * 이면 십자가의 중심임
        for dx, dy in dxdy:
            nx, ny = i+dx, j+dy
            if not(0<=nx<N and 0<=ny<M): break
            if arr[nx][ny]=='.': break
        else :
            # 십자가의 중심인 경우,
            flag =True
            k = 1
            visited[i][j]=True
            while flag:
                #한 둘레를 방문처리
                for dx, dy in dxdy:
                    nx, ny = i + dx*k, j + dy*k
                    visited[nx][ny]=True
                # 다음 둘레를 갈 수 있는지 봄
                # 더이상 못가면 while문 break
                k+=1
                for dx, dy in dxdy:
                    nx, ny = i + dx*k, j + dy*k
                    if not (0 <= nx < N and 0 <= ny < M):
                        flag = False
                        break
                    if arr[nx][ny] == '.':
                        flag = False
                        break
            # 한칸 더 가서 확있했으니까 실제로 길이는 k-1임
            ans.append((i+1, j+1, k-1))

# *인데 방문을 안한 곳이 있으면 false 처리
result = True
for i in range(N):
    for j in range(M):
        if arr[i][j]=='*' and not visited[i][j]:
            result=False
            break
if result:
    print(len(ans))
    for ele in ans:
        print(*ele)
else : print(-1)