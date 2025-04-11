from collections import deque

N, M, L, T, K = map(int, input().split())
dxdy = ((0, 0), (-1, -1),  (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
arr = [list(input()) for _ in range(N)]
teacher = [set() for _ in range(T//10+1)]
for l in range(L):
    p = int(input())
    for pi in range(p):
        tx, ty = map(int, input().split())
        for i in range(pi, T//10+1, p):
            for dx, dy in dxdy:
                tnx, tny = tx+dx-1, ty+dy-1
                if not(0<=tnx<N and 0<=tny<M): continue
                if (tnx, tny) in {(0, 0), (N-1, M-1)}: continue
                teacher[i].add((tnx, tny))

q = deque([(0, 0, 5, 0)])
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
visited[0][0][0]=1

while q:
    x, y, t, goal = q.popleft()

    if t>T:
        print('SAD')
        break

    ntt = t//10
    if (x, y) in teacher[ntt]:
        visited[x][y][goal]=0
        continue

    if goal:
        if max(x, y)+t-1<=T:
            q.append((x, y, t+10, goal))
    elif max(M-1-y, N-1-x)+max(N, M)-1+t<=T:
        q.append((x, y, t + 10, goal))

    if t%10==5:
        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<M): continue
            if visited[nx][ny][goal]: continue
            if (nx, ny) in teacher[ntt]: continue
            if arr[nx][ny]=='#': continue

            if goal and (nx, ny)==(0, 0):
                print('YUMMY')
                break

            if (nx, ny)==(N-1, M-1) and not goal:
                visited[nx][ny][goal]=1
                if K%10==0:
                    q.append((nx, ny, t+K, 1))
                else:
                    q.append((nx, ny, ((t+K-5)//10+1)*10+5, 1))
            else:
                visited[nx][ny][goal]=1
                q.append((nx, ny, t+10, goal))
        else:
            continue
        break
else:
    print('SAD')