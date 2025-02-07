T = int(input())
dxdy = ((0,1),(0,-1),(1,0),(-1,0))
for tc in range(1, T+1):
    N = int(input())
    arr = [[11]*(N+2)]+[[11]+list(map(int, input().split()))+[11] for _ in range(N)]+[[11]*(N+2)]
    active = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            for dx, dy in dxdy:
                nx, ny = i+dx, j+dy
                if arr[nx][ny]>=arr[i][j]:
                    break
            else: active.append(arr[i][j])
    if len(active)<=1:
        ans = -1
    else :
        ans = max(active)-min(active)
    print(f'#{tc} {ans}')
