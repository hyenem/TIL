def makepipe(i, j):
    if j==M-1:
        return 1

    for k in range(-1, 2):
        if not(0<=i+k<N): continue
        if arr[i+k][j+1]: continue
        arr[i+k][j+1]=1
        result = makepipe(i+k, j+1)
        if result: return 1
    return 0

N, M = map(int, input().split())
arr = [list(map(lambda x: 1 if x=='x' else 0, input())) for _ in range(N)]
ans = 0

maxx = N
for j in range(M):
    cnt = 0
    for i in range(N):
        if arr[i][j]==0:
            cnt+=1
    maxx = min(maxx, cnt)

for i in range(N):
    ans += makepipe(i, 0)
    if ans>=maxx: break

print(ans)