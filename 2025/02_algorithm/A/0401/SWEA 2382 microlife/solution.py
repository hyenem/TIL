T = int(input())
dxdy = (0, (-1, 0), (1, 0), (0, -1), (0, 1))
reverse_d = [0, 2, 1, 4, 3]

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    micro = [tuple(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        arr = [[[] for _ in range(N)] for _ in range(N)]
        for x, y, n, d in micro:
            dx, dy = dxdy[d]
            nx, ny = x+dx, y+dy
            if nx in {0, N-1} or ny in {0, N-1}:
                d = reverse_d[d]
                n = n//2
            arr[nx][ny].append((n, d))

        micro = []
        for i in range(N):
            for j in range(N):
                if len(arr[i][j])==0: continue
                elif len(arr[i][j])==1:
                    n, d = arr[i][j][0]
                    micro.append((i, j, n, d))
                else :
                    arr[i][j].sort()
                    d = arr[i][j][-1][1]
                    n = sum(x[0] for x in arr[i][j])
                    micro.append((i, j, n, d))

    ans = sum(x[2] for x in micro)
    print(f'#{tc} {ans}')