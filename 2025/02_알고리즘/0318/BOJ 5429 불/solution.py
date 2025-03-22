T = int(input())
for _ in range(T):
    M, N = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    dxdy = ((0, 1), (0, -1), (1, 0), (-1, 0))
    fire = []
    person = []
    for i in range(N):
        for j in range(M):
            if arr[i][j]=='@':
                person.append((i, j))
            elif arr[i][j]=='*':
                fire.append((i, j))

    ans = 0
    time = 0
    while person:
        time += 1

        # 불먼저 번지기
        nfire = []
        while fire:
            x, y = fire.pop()
            for dx, dy in dxdy:
                nx, ny = x+dx, y+dy
                if not(0<=nx<N and 0<=ny<M): continue
                if arr[nx][ny] in {'#', '*'}: continue
                arr[nx][ny]='*'
                nfire.append((nx,ny))
        fire = nfire

        # 사람 이동
        nperson = []
        while person:
            x, y = person.pop()
            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy
                # 빠져나갔으면 정답 갱신
                if not (0 <= nx < N and 0 <= ny < M):
                    ans = time
                    break
                if arr[nx][ny] in {'#', '*', '@'}: continue
                arr[nx][ny] = '@'
                nperson.append((nx, ny))

        if ans:
            print(ans)
            break

        person = nperson

    else : print('IMPOSSIBLE')