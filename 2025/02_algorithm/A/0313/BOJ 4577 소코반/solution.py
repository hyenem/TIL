tc = 0
while True:
    tc+=1
    N, M = map(int,input().split())
    if N==0: break

    arr = [list(input()) for _ in range(N)]
    goal = set()
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] in {'+', 'W', 'B'}:
                if arr[i][j]=='W':
                    x, y = i, j

                if arr[i][j]=='B':
                    cnt += 1
                    arr[i][j]='b'
                else :
                    arr[i][j]='.'
                goal.add((i, j))

            if arr[i][j]=='w':
                x, y = i, j
                arr[i][j]='.'

    cmds = list(input())
    dir = {'U': (-1, 0), 'L': (0, -1), 'D': (1, 0), 'R': (0, 1)}
    for d in cmds:
        if cnt ==len(goal): break

        dx, dy = dir[d]
        nx, ny = x+dx, y+dy
        if arr[nx][ny]=='#': continue
        elif arr[nx][ny]=='b':
            if not(0<=nx+dx<N and 0<=ny+dy<M): continue
            if arr[nx+dx][ny+dy]=='.':
                if (nx, ny) in goal: cnt -= 1
                if (nx+dx, ny+dy) in goal: cnt += 1
                arr[nx + dx][ny + dy] = 'b'
                arr[nx][ny]='.'
                x, y = nx, ny

        else :
            x, y = nx, ny

    arr[x][y]='w'

    for gx, gy in goal:
        if arr[gx][gy]=='b':
            arr[gx][gy]='B'
        elif arr[gx][gy]=='w':
            arr[gx][gy]='W'
        elif arr[gx][gy]=='.':
            arr[gx][gy]='+'


    if cnt==len(goal): result='complete'
    else: result = 'incomplete'

    print(f'Game {tc}: {result}')
    for ele in arr:
        print(''.join(ele))


