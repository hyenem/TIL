import heapq

while True:
    N, M = map(int, input().split())
    if N==0: break

    arr = [list(input()) for _ in range(N)]
    sign = []
    while True:
        data = input()
        if not data: break
        i, d, a, b = data.split()
        if d=='-': d = 0
        else : d = 1
        sign.append((d, int(a), int(b)))

    truck = []
    for i in range(N):
        for j in range(M):
            if arr[i][j]=='A':
                truck.append((0, i, j))
            elif arr[i][j]=='B':
                goal = (i,j)
                arr[i][j]='#'

    visited = [[N*M*1000]*M for _ in range(N)]
    while truck:
        t, x, y = heapq.heappop(truck)
        if (x, y)==goal:
            print(t)
            break

        if visited[x][y]<t: continue
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<M): continue
            if arr[nx][ny]=='#':
                if visited[nx][ny]>t+1:
                    visited[nx][ny]=t+1
                    heapq.heappush(truck, (t+1, nx, ny))
            elif 0<=ord(arr[nx][ny])-ord('0')<10:
                idx = ord(arr[nx][ny])-ord('0')
                d, a, b = sign[idx]

                if dx==0: wd = 0
                else : wd = 1

                if d==0:
                    first, second = a, b
                else : first, second = b, a

                if d==wd:
                    if t%(a+b)<first:
                        nt = t+1
                    else :
                        nt = (t//(a+b)+1)*(a+b)+1
                else :
                    if t%(a+b)<first:
                        nt = (t//(a+b))*(a+b)+first+1
                    else :
                        nt = t+1
                if visited[nx][ny]>nt:
                    visited[nx][ny]=nt
                    heapq.heappush(truck, (nt, nx, ny))

    else : print("impossible")
