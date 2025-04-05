'''2회독
제출횟수 : 1회
풀이시간 : 9분

* 이전 코드와 비교해서 과도한 가지치기는 하지 않고
* 깔끔한 코드가 됨

* 크게 피드백 할 내용 없음
'''

from collections import deque

def fire():
    global ans

    tmpans = N*M
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j]: continue
            if arr[i][j]==1: tmpans -= 1

            if arr[i][j]==2:

                tmpans -= 1
                visited[i][j]=1
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in ((-1,0), (0, 1), (1, 0), (0, -1)):
                        nx, ny = x+dx, y+dy
                        if not(0<=nx<N and 0<=ny<M): continue
                        if visited[nx][ny]: continue
                        if arr[nx][ny]==0:
                            visited[nx][ny]=1
                            tmpans -= 1
                            q.append((nx, ny))

    ans = max(ans, tmpans)


def btk(idx, cnt):
    if cnt==3:
        fire()
        return

    for i in range(idx+1, N*M):
        x, y = i//M, i%M
        if arr[x][y]==0:
            arr[x][y]=1
            btk(i, cnt+1)
            arr[x][y]=0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
btk(-1, 0)
print(ans)

''' 1회독
제출횟수 : 1회
풀이시간 : 19분

실행시간 : 356ms
메모리 : 114880KB
코드길이 : 1107B

* 명심할 것
디버깅 과정에서 TC하나만 보지말고, 다른 것들도 보면서
답과의 차이에 규칙성이 있는지
특정 TC만 틀린건지 아니면 다 틀린건지 확인해보기

구상 : 2분
* 벽 위치 결정해주고 BFS 해주면 되겠다
* 벽 위치를 그리디하게 결정하기 어려울 것 같다.
* 3개 고르는 거니까 M*N 최대 64 중에서 조합해야겠다
* 대강의 최대 시간 복잡도 : (N*M)**4 이므로 최대 2**24(가능)

구현 : 10분
* btk, bfs 함수 뽑아내기
* 처음에 wall을 들고다녔다가 곧 들고다닐 필요가 없다는걸 꺠닫고 버림

디버깅 : 7분
* 새로 세운 벽 3개를 기존 빈칸에서 빼줘야한다는 걸 놓침!!!!!

리팩토링
* 가지치기 고민해봄
* cnt가 이미 정답보다 작아지면 더이상 bfs 돌릴 필요 없음
* 주변이 다 빈칸으로만 채워지면 거기에 벽을 세울 이유가 없음
    * 팔방 보면서 빈칸이 아닌게 있는지 채크
    * 이때 범위 바깥으로 빠져나가는 것 처리 잘해줘야함(범위 바깥으로 빠져나가도 break

from collections import deque

def bfs():
    global ans

    # 기존 빈 칸의 개수
    cnt = can
    visited =[[0]*M for _ in range(N)]
    q = deque(start)
    for x, y in q:
        visited[x][y]=1

    while q:
        x, y = q.popleft()
        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<M): continue
            if visited[nx][ny]: continue
            if arr[nx][ny]==0:
                visited[nx][ny]=1
                cnt -=1
                # 가지치기1
                if cnt<=ans: return
                q.append((nx, ny))

    ans = max(ans, cnt)

def btk(idx, cnt):
    # 벽 3개 세우면 바이러스 퍼트리기
    if cnt==3:
        bfs()
        return

    # 전체를 한줄로 만들어서 돈다고 생각
    for i in range(idx+1, N*M):
        if arr[i//M][i%M]!=0: continue

        # 가지치기2 : 팔방이 빈칸으로 채워져있으면 벽을 세울 이유가 없음
        for dx, dy in ((0,1), (1,1), (-1, 1), (1, 0), (-1, 0), (0,-1), (1,-1), (-1,-1)):
            if not(0<=i//M+dx<N and 0<=i%M+dy<M): continue
            if arr[i//M+dx][i%M+dy]!=0:
                break
        else : continue

        arr[i//M][i%M]=1
        btk(i, cnt+1)
        arr[i // M][i % M] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dxdy = ((0,1), (0,-1), (1,0), (-1,0))
can = 0
start = []
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            can +=1                 # 빈칸의 개수
        elif arr[i][j]==2:
            start.append((i,j))     # 처음 바이러스 위치

ans = 0

btk(-1, 0)
# 벽 세운거 3개 제외하기
print(ans-3)
'''