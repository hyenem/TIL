def drop(arr, w, h, idx):
    global ans
    for i in range(2, 6):
        for j in w:
            if arr[i][j]!=0:
                i-=1
                break
        else: continue
        break

    for hi in range(h):
        for j in w:
            arr[i-hi][j]=idx

    end = 0
    while not end:
        end = 1
        for i in range(2, 6):
            if arr[i].count(0)==0:
                end = 0
                ans += 1
                del arr[i]
                arr.insert(0, [0]*4)

        visited = [[0]*4 for _ in range(6)]
        for i in range(5, -1, -1):
            for j in range(4):
                if arr[i][j]==0 or visited[i][j]: continue
                visited[i][j]=1
                block = [(i, j)]
                for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    nx, ny = i+dx, j+dy
                    if not(0<=nx<6 and 0<=ny<4): continue
                    if visited[nx][ny]: continue
                    if arr[nx][ny]==arr[i][j]:
                        visited[nx][ny]=1
                        block.append((nx, ny))

                for down in range(1, 6):
                    for x, y in block:
                        nx = x+down
                        if (not 0<=nx<6 )or arr[nx][y] not in {arr[x][y], 0}:
                            down -= 1
                            break
                    else: continue
                    break

                if down!=0:
                    for x, y in block:
                        didx = arr[x][y]
                        arr[x][y]=0
                    for x, y in block:
                        arr[x+down][y]=didx

    for i in range(2):
        if sum(arr[i])!=0:
            arr.pop()
            arr.insert(0, [0]*4)




N = int(input())
cmds = [list(map(int, input().split())) for _ in range(N)]

green = [[0]*4 for _ in range(6)]
blue = [[0]*4 for _ in range(6)]

ans = 0
for idx, (t, x, y) in enumerate(cmds, start=1):
    if t==1:
        h = (x, )
        w = (y, )
    elif t==2:
        h = (x,)
        w = (y, y+1)
    else:
        h = (x, x+1)
        w = (y,)

    drop(green, w, len(h), idx)
    drop(blue, h, len(w), idx)

print(ans)
ans2 = 0
for i in range(6):
    ans2+=4-green[i].count(0)
    ans2+=4-blue[i].count(0)
print(ans2)