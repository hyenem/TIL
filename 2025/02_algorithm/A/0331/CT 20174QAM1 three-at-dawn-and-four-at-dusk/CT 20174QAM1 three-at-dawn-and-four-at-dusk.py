def btk(idx, dist):
    global ans

    if idx==N:
        ans = min(abs(dist), ans)
        return

    if len(dawn)!=N//2:
        ndist =dist
        for i in dawn:
            ndist += arr[i][idx]+arr[idx][i]
        dawn.append(idx)
        btk(idx+1, ndist)
        dawn.pop()

    if len(dusk)!=N//2:
        ndist = dist
        for i in dusk:
            ndist -= arr[i][idx]+arr[idx][i]
        dusk.append(idx)
        btk(idx+1, ndist)
        dusk.pop()


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dawn = [0]
dusk = []

ans = 100*N*N
btk(1, 0)
print(ans)