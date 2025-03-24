def choose(idx, cnt, minforhome):
    global minimum
    if cnt==M:
        minimum = min(minimum, sum(minforhome))
        return
    tmp = minforhome[:]
    for i in range(idx+1, len(chicken)):
        for j in range(len(home)):
            minforhome[j]=min(minforhome[j], dis[i][j])
        choose(i, cnt+1, minforhome)
        minforhome = tmp[:]


N, M = map(int,input().split())
home = []
chicken = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j]==1:
            home.append((i, j))
        elif tmp[j]==2:
            chicken.append((i, j))

dis = [[0]*len(home) for _ in range(len(chicken))]
for i in range(len(chicken)):
    for j in range(len(home)):
        dis[i][j]=abs(home[j][0]-chicken[i][0])+abs(home[j][1]-chicken[i][1])

minimum = 4*N*N
choose(-1, 0, [2*N]*len(home))
print(minimum)