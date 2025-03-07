def solution(idx, cnt, acc):
    global ans
    # 별이 2개 만들어졌으면 정답 갱신
    if cnt==2:
        ans = max(ans, acc)
        return
    # 별의 중심으로 조합만들기
    for i in range(idx+1, N*M):
        x, y = i//M, i%M
        # 이미 방문했거나 별이 될 수 없는 칸은 넘어가기
        if visited[x][y]: continue
        if arr[x][y]=='.': continue

        maxlenth = 0
        flag = True
        # 해당 칸을 중심으로 만들 수 있는 별의 최대 길이 계산
        while flag:
            maxlenth+=1
            for dx, dy in ((0,1), (0,-1), (1, 0), (-1, 0)):
                nx, ny = x+dx*maxlenth, y+dy*maxlenth
                if not(0<=nx<N and 0<=ny<M):
                    flag = False
                    break
                if visited[nx][ny]:
                    flag = False
                    break
                if arr[nx][ny]=='.':
                    flag = False
                    break

        # 한 칸씩 늘려가면서 btk
        for i in range(maxlenth):
            # 한칸 늘리고
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = x + dx * i, y + dy * i
                visited[nx][ny]=True
            # 해당 별 누적해서 다음 별 만들기
            solution(i, cnt+1, acc*(4*i+1))
        # 전체 다 간 다음에 전부다 방문처리 취소
        for i in range(maxlenth):
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = x + dx * i, y + dy * i
                visited[nx][ny]=False


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
ans = 0
solution(-1, 0, 1)
print(ans)