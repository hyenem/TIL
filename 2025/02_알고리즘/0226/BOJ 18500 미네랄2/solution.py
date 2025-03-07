def shoot(turn, shootx):
    shooty = -1
    if turn ==0:
        for j in range(M):
            if arr[shootx][j]=='x':
                arr[shootx][j]='.'
                shooty = j
                break
    else :
        for j in range(M-1, -1, -1):
            if arr[shootx][j]=='x':
                arr[shootx][j]='.'
                shooty = j
                break
    return shooty

def move_cluster(nx, ny):
    visited[nx][ny]=True
    cluster = [(nx, ny)]
    clustertf = [[False]*M for _ in range(N)]
    idx = 0
    flag = True
    while idx<len(cluster):
        x, y = cluster[idx]
        clustertf[x][y]=True
        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<M): continue
            if arr[nx][ny]=='.': continue
            if visited[nx][ny]: continue
            if nx==N-1:
                flag = False
            cluster.append((nx, ny))
            visited[nx][ny]=True
        idx+=1

    if not flag: return False

    fall = N
    for x, y in cluster:
        for i in range(x+1, N):
            if arr[i][y]=='x':
                if clustertf[i][y]: break
                fall=min(fall, i-x-1)
                break
        else : fall = min(fall, N-x-1)

    for x, y in cluster:
        arr[x][y]='.'
    for x, y in cluster:
        arr[x+fall][y]='x'

    return True

N, M = map(int, input().split())
arr=[list(input()) for _ in range(N)]
K = int(input())
lst = list(map(int, input().split()))
dxdy = ((-1,0), (1, 0), (0,1), (0, -1))

for k in range(K):
    shootx = N-lst[k]
    shooty = shoot(k%2, shootx)
    if shooty==-1 : continue

    visited = [[0]*M for _ in range(N)]
    for dx, dy in dxdy:
        nx, ny = shootx+dx, shooty+dy
        if not(0<=nx<N and 0<=ny<M): continue
        if arr[nx][ny]=='.': continue
        if visited[nx][ny]: continue
        result = move_cluster(nx, ny)
        if result: break

for ele in arr:
    print(''.join(ele))
