T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = -1
    for i in range(N):
        for j in range(N):
            ux, uy = i, j
            for l in range(1, j+1):
                lx, ly = i+l, j-l
                if not 0<=lx<N: continue

                for r in range(1, N-j):
                    rx, ry = i+r, j+r
                    dx, dy = rx+l, ry-l
                    if not 0<=dx<N: continue

                    tmpcnt = (ry-ly)*2
                    if tmpcnt<=cnt : continue

                    selected = set()

                    x, y = ux, uy
                    selected.add(arr[x][y])
                    visited = [[0]*N for _ in range(N)]
                    while (x, y)!=(rx, ry):
                        x, y = x+1, y+1
                        visited[x][y]=1
                        if arr[x][y] in selected:
                            break
                        selected.add(arr[x][y])
                    else:
                        while (x, y)!=(dx, dy):
                            x, y = x+1, y-1
                            visited[x][y] = 1

                            if arr[x][y] in selected:
                                break
                            selected.add(arr[x][y])
                        else:
                            while (x, y) != (lx, ly):
                                x, y = x - 1, y - 1
                                visited[x][y] = 1

                                if arr[x][y] in selected:
                                    break
                                selected.add(arr[x][y])
                            else :
                                while (x, y) != (ux+1, uy-1):
                                    x, y = x - 1, y + 1
                                    visited[x][y] = 1

                                    if arr[x][y] in selected:
                                        break
                                    selected.add(arr[x][y])
                                else:
                                    cnt = tmpcnt
    print(f'#{tc} {cnt}')