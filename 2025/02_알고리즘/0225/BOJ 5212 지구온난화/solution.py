N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

landx = []
landy = []
sea = []
for i in range(N):
    for j in range(M):
        if arr[i][j]=='X':
            cnt = 0
            for dx, dy in ((0,1), (0,-1), (1, 0), (-1, 0)):
                nx, ny = i+dx, j+dy
                if not (0<=nx<N and 0<=ny<M): continue
                if arr[nx][ny]!='.': cnt+=1

            if cnt>=2:
                landx.append(i)
                landy.append(j)
            else :
                sea.append((i,j))
while sea:
    x, y = sea.pop()
    arr[x][y]='.'

for i in range(min(landx), max(landx)+1):
    print(''.join(arr[i][min(landy): max(landy)+1]))
