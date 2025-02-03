T = int(input())

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 몇번째 코어인지, 몇개의 코어를 사용해왔는지
# 얼마만큼의 길이가 누적되어 있는지, 어디를 방문했는지
def compute(idx, cnt, summ, visited):
    ans[cnt] = min(ans[cnt], summ)
    if idx >= len(cores):
        return
    compute(idx+1, cnt, summ, visited)
    for direction in range(4):
        nx = cores[idx][0]+dx[direction]
        ny = cores[idx][1]+dy[direction]
        flag = True
        while 0<=nx<N and 0<=ny<N:
            if visited[nx]&(1<<ny)==1:
                flag = False
                break
            nx += dx[direction]
            ny += dy[direction]
        if flag:
            newvisited = visited[:]
            nx = cores[idx][0] + dx[direction]
            ny = cores[idx][1] + dy[direction]
            newsumm = 0
            while 0 <= nx < N and 0 <= ny < N:
                newvisited[nx] |= (1<<ny)
                newsumm += 1
                nx += dx[direction]
                ny += dy[direction]
            if newsumm != 0:
                compute(idx+1, cnt+1, summ+newsumm, newvisited)


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    cores = []
    corenum = 0

    cnt_max = 0
    summ_min = N*N
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                visited[i] |= (1<<j)
                if i not in {0, N-1} and j not in {0, N-1}:
                    cores.append((i, j))

    ans = [N*N+1]*(len(cores)+1)
    compute(0, 0, 0, visited)
    print(ans)
    for i in range(len(cores), -1, -1):
        if ans[i]!=N*N+1:
            print(f'#{tc} {ans[i]}')
            break

