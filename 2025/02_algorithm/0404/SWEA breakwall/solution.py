from collections import deque

def drop(idx):
    q = deque()
    for i in range(N):
        if arr[i][idx]!=0:
            q.append((i, idx, arr[i][idx]))
            arr[i][idx]=0
            break
    while q:
        x, y, num = q.popleft()
        for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            for k in range(num):
                nx, ny = x+k*dx, y+k*dy
                if not(0<=nx<N and 0<=ny<M): break
                if arr[nx][ny]>=2:
                    q.append((nx, ny, arr[nx][ny]))
                arr[nx][ny]=0

    for j in range(M):
        acc = 0
        for i in range(N-1, -1, -1):
            if arr[i][j]==0:
                acc+=1
            else:
                arr[i+acc][j], arr[i][j] = arr[i][j], arr[i+acc][j]



def btk(cnt):
    global ans, arr
    if cnt==K:
        tmpans = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j]!=0:
                    tmpans += 1
        ans = min(ans, tmpans)
        return

    tmp = [ele[:] for ele in arr]
    for i in range(M):
        drop(i)
        btk(cnt+1)
        arr = [ele[:] for ele in tmp]


T = int(input())
for tc in range(1, T+1):
    K, M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = M*N+1
    btk(0)
    print(f'#{tc} {ans}')

