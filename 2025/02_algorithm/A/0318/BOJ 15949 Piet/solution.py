import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0))
sx, sy = 0, 0
DP, CC = 0, 1
ans =[]
visited = [[0]*M for _ in range(N)]
dic = {}
while True:
    ans.append(arr[sx][sy])
    if visited[sx][sy]:
        dpcc = dic[(sx, sy)]
    else :
        visited[sx][sy]=1
        q = [(sx, sy)]
        idx = 0
        dpcc = [[sy, sx, sx], [sx, sy, sy], [sy, sx, sx], [sx, sy, sy]]
        while idx<len(q):
            x, y = q[idx]
            idx += 1
            for dx, dy in dxdy:
                nx, ny = x+dx, y+dy
                if not (0<=nx<N and 0<=ny<M): continue
                if visited[nx][ny]: continue
                if arr[x][y]!=arr[nx][ny]: continue

                visited[nx][ny]=1
                q.append((nx, ny))

                if nx>dpcc[1][0]: dpcc[1]=[nx, ny, ny]
                elif nx==dpcc[1][0]:
                    dpcc[1][1]=max(dpcc[1][1], ny)
                    dpcc[1][2]=min(dpcc[1][2], ny)

                if nx<dpcc[3][0]: dpcc[3]=[nx, ny, ny]
                elif nx==dpcc[3][0]:
                    dpcc[3][1] = min(dpcc[3][1], ny)
                    dpcc[3][2] = max(dpcc[3][2], ny)

                if ny>dpcc[0][0]: dpcc[0] = [ny, nx, nx]
                elif ny==dpcc[0][0]:
                    dpcc[0][1]=min(dpcc[0][1], nx)
                    dpcc[0][2]=max(dpcc[0][2], nx)

                if ny<dpcc[2][0]: dpcc[2] = [ny, nx, nx]
                elif ny==dpcc[2][0]:
                    dpcc[2][1]=max(dpcc[2][1], nx)
                    dpcc[2][2]=min(dpcc[2][2], nx)
        while q:
            x, y = q.pop()
            dic[(x, y)]=dpcc

    for k in range(4):

        dx, dy = dxdy[DP]
        if DP%2==0:
            y, x = dpcc[DP][0], dpcc[DP][CC]
        else :
            x, y = dpcc[DP][0], dpcc[DP][CC]
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M and arr[nx][ny]!='X':
            sx, sy = nx, ny
            break

        CC = 3-CC
        if DP%2==0:
            y, x = dpcc[DP][0], dpcc[DP][CC]
        else :
            x, y = dpcc[DP][0], dpcc[DP][CC]
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M and arr[nx][ny]!='X':
            sx, sy = nx, ny
            break
        DP = (DP + 1) % 4
    else : break

print(''.join(ans))