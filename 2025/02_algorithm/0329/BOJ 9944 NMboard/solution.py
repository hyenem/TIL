def dfs(x, y, cnt, depth):
    global tmpans
    if tmpans!=-1 and tmpans<=depth: return

    if cnt==K:
        tmpans = depth
        return

    for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nx, ny = x+dx, y+dy
        if not(0<=nx<N and 0<=ny<M) or arr[nx][ny]=='*': continue

        stack = [(nx, ny)]
        arr[nx][ny]='*'
        tmpcnt = 1
        while 0<=nx+dx<N and 0<=ny+dy<M and arr[nx+dx][ny+dy]!='*':
            tmpcnt += 1
            nx, ny = nx+dx, ny+dy
            stack.append((nx, ny))
            arr[nx][ny] = '*'

        dfs(nx, ny, cnt+tmpcnt, depth+1)

        while stack:
            nx, ny = stack.pop()
            arr[nx][ny]='.'


ans = []
while True:
    try:
        N, M = map(int, input().split())
        arr = [list(input()) for _ in range(N)]
        K = 0
        tmpans = -1
        for i in range(N):
            for j in range(M):
                if arr[i][j]=='*': continue
                K+=1

        for i in range(N):
            for j in range(M):
                if arr[i][j]=='*': continue
                arr[i][j]='*'
                dfs(i, j, 1, 0)
                arr[i][j]='.'

        ans.append(tmpans)
    except:
        for i in range(len(ans)):
            print(f'Case {i+1}: {ans[i]}')
        break