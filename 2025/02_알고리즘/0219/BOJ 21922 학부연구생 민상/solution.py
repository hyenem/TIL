'''
제출횟수 : 2회
실행시간 : 3116 ms
메모리 : 622892KB

* 무한 루프 돌 수 있다는 사실을 간과함
* 한 칸에 특정 방향으로 갔으면 그 이후로는 이전 방문과 루트가 똑같음
'''

def check(i, j):
    global ans
    for d in range(4):
        x, y = i, j
        while True:
            dx, dy = dxdy[d]
            x += dx
            y += dy
            if not(0<=x<N and 0<=y<M): break
            if visited[x][y][d]: break

            if not visited[x][y][4]: ans+=1
            visited[x][y][d]=True
            visited[x][y][4]=True

            if d in {2, 3} and arr[x][y]==1: break
            if d in {0, 1} and arr[x][y]==2: break
            if arr[x][y]==3:
                d = 3 - d
            elif arr[x][y]==4:
                d = (d + 2) % 4


dxdy = [(1,0), (-1, 0), (0,1), (0,-1)]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 각 방향별 방문을 표시하고, 마지막 인덱스는 한번이라도 방문하면 표시
visited = [[[False]*5 for _ in range(M)] for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j]==9:
            if not visited[i][j][4]: ans +=1
            visited[i][j]=[True, True, True, True, True]
            check(i, j)
print(ans)