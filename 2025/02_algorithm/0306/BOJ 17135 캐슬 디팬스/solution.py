
def play(p1, p2, p3):
    global ans

    tmpans = 0
    mapp = [ele[:] for ele in arr]
    tmpenemy = enemy
    while tmpenemy:
        attack = set()
        for p in (p1, p2, p3):
            flag = 0
            for d in range(D):
                for k in range(-d, d+1):
                    if not(0<=p+k<M): continue
                    if mapp[N-1-d+abs(k)][p+k]==1:
                        attack.add((N-1-d+abs(k), p+k))
                        flag = 1
                        break
                if flag: break
        tmpans+=len(attack)
        tmpenemy-=len(attack)
        for x, y in attack:
            mapp[x][y]=0

        tmpenemy-=sum(mapp[N-1])
        mapp.pop()
        mapp.insert(0, [0]*M)

    ans = max(ans, tmpans)



N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

enemy = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            enemy += 1


ans = 0
for i in range(M):
    for j in range(i+1, M):
        for k in range(j+1, M):
            play(i, j, k)

print(ans)