def solution(x, y):
    if (x, y) == (N, M):
        ans[len(visit)]+=1
    for dx, dy in ((0,1), (1,0)):
        nx, ny = x+dx, y+dy
        if 0<nx<=N and 0<ny<=M:
            if arr[nx][ny]==0:
                solution(nx, ny)
            else :
                if not visit or visit[-1]<arr[nx][ny]:
                    visit.append(arr[nx][ny])
                    solution(nx, ny)
                    visit.pop()

N, M, C = map(int, input().split())
arr = [[0]*(M+1) for _ in range(N+1)]
for i in range(C):
    x, y = map(int, input().split())
    arr[x][y] = i+1

visit = []
ans = [0]*(C+1)
solution(1,1)
print(*ans)