'''2회독
제출횟수 : 1회
풀이시간 : 30분

* 배열 복사해서 이전 상태로 참조해야하는지! 변한것 그대로 ㅊ참조해야하는지 채크해라!!!!!
'''

def lotate(l):
    tmp = [ele[:] for ele in arr]
    L = 2**l
    for i in range(0, N, L):
        for j in range(0, N, L):
            sxsy = ((0, 0), (0, L//2), (L//2, L//2), (L//2, 0))
            for s in range(4):
                sx, sy = sxsy[s]
                bsx, bsy = sxsy[(s-1)%4]
                for x in range(L//2):
                    for y in range(L//2):
                        arr[i+sx+x][j+sy+y]=tmp[i+bsx+x][j+bsy+y]

n, Q = map(int, input().split())
N = 2**n
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
arr= [list(map(int, input().split())) for _ in range(N)]
cmds = list(map(int, input().split()))
for l in cmds:
    lotate(l)

    tmp = [ele[:] for ele in arr]
    for i in range(N):
        for j in range(N):
            if tmp[i][j]==0: continue
            cnt = 0
            for dx, dy in dxdy:
                nx, ny = i+dx, j+dy
                if 0<=nx<N and 0<=ny<N and tmp[nx][ny]:
                    cnt+=1
            if cnt<3:
                arr[i][j]-=1

ans1= 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j]: continue
        if arr[i][j]==0: continue

        q = [(i, j)]
        visited[i][j]=1
        idx = 0
        while idx<len(q):
            x, y = q[idx]
            idx += 1

            for dx, dy in dxdy:
                nx, ny = x+dx, y+dy
                if not(0<=nx<N and 0<=ny<N): continue
                if arr[nx][ny]==0: continue
                if visited[nx][ny]: continue

                visited[nx][ny]=1
                q.append((nx,ny))

        ans1 = max(ans1, len(q))

ans2 = sum(map(sum, arr))
print(ans2)
print(ans1)

'''
제출횟수 : 1회
풀이시간 : 31분

실행시간 : 500ms -> 472mx
메모리 : 119096KB -> 119056KB

! 명심할 것 !
[1]
동시에 여러가지 의심이 들면 다 정리해두고 하나씩 채크하기
디버깅 과정에서 아! 이거 먼저 확인하고 저거 확인해봐야겠다에서
'저거'가 원인인 경우가 많음
근데 인제 까먹고 있었던,,,

[2]
문제의 구하는 답이 뭔지 명확히 이해할 것
두번쨰 정답(가장 큰 블럭의 칸의 개수)를
처음에는 블럭의 개수로 오해했다가, 다음에는 가장 큰 블럭의 얼음의 양으로 오해함

구상 : 5분
* 90도 회전할 때 인덱스 처리 어떻게 할지 결정하는데 시간을 사용함

구현 : 15분
디버깅 : 11분
[1] (7분)두번쨰 정답을 이해하는데 시간을 사용
[2] (4분) melt에서 배열을 복사하지 않고, 바로 해당 배열에 반영해서 오류가 발생


리팩토링
* N이 배열의 크기가 아닌게 계속 신경쓰였음
* 매번 2**N의 연산을 할 이유도 없을 것 같아서
* rN(realN) 이라는 변수를 만들어서 2**N을 관리함

[시간복잡도]
대강 (2**(N+1))*Q -> 최대 대강 10^6정도

[테스트케이스] : 처음부터 얼음이 하나도 없었던 경우
2 10
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 2 0 1 2 0 1 2 0 1

from collections import deque

def rotate(l):
    # 복사 배열보고 돌려서 기존 배열 채우기
    tmparr = [ele[:] for ele in arr]
    M = 2**l
    for i in range(2**(N-l)):
        for j in range(2**(N-l)):
            # x, y는 각 점의 시작 행, 열 인덱스
            x, y = i*M, j*M
            # 90도 회전인데 시작이 x, y 좌표인
            for ni in range(M):
                for nj in range(M):
                    arr[x+ni][y+nj]=tmparr[x+M-nj-1][y+ni]

def melt():
    # 이번에 녹인 것 다른 칸이 영향을 받아서는 안되니까
    # 인접한 얼음 개수는 tmp 배열로 찾고, 녹이는건 기존 arr에
    tmparr = [ele[:] for ele in arr]

    for i in range(rN):
        for j in range(rN):
            if tmparr[i][j]==0: continue

            # 얼음이 아닌 인접한 칸의 개수 세기
            cnt = 0
            for dx, dy in dxdy:
                nx, ny = i+dx, j+dy
                if not(0<=nx<rN and 0<=ny<rN) or tmparr[nx][ny]==0:
                    cnt+=1
                    # 인접한 칸이 2개 이상이 되면 그만
                    if cnt==2: break

            # 2개 이상인 경우 녹이기
            if cnt==2:
                arr[i][j] -= 1

def bfs(x, y):
    global anscnt

    # 이번 블럭의 칸수 저장
    tmpcnt = 0
    q = deque([(x, y)])
    visited[x][y]=1
    while q:
        x, y = q.popleft()
        tmpcnt += 1
        # 전체 얼음 양에 추가하기
        anscnt += arr[x][y]

        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < 2 ** N and 0 <= ny < 2 ** N):
                continue
            if visited[nx][ny]: continue
            if arr[nx][ny]==0: continue

            visited[nx][ny]=1
            q.append((nx, ny))

    return tmpcnt

N, Q = map(int, input().split())
rN = 2**N      # 실제 배열 사이즈
arr = [list(map(int, input().split())) for _ in range(rN)]
L = list(map(int, input().split()))
dxdy = ((0,1), (0, -1), (1, 0), (-1, 0))
visited = [[0]*(rN) for _ in range(rN)]

for q in range(Q):
    # 돌리기
    # l이 0이면 모든 칸이 다 쪼개지는 거니까 돌리는게 의미가 없음
    if L[q]!=0:
        rotate(L[q])

    # 얼음 3개 이상 아니면 녹이기
    melt()

anscnt = 0
maxcnt = 0

# 정답 찾기
for i in range(rN):
    for j in range(rN):
        if arr[i][j]==0: continue
        if visited[i][j] : continue
        # 리턴 값은 이번 얼음의 칸 수
        # 최댓값 갱신하기
        tmpcnt = bfs(i, j)
        maxcnt = max(maxcnt, tmpcnt)

print(anscnt)
print(maxcnt)
'''