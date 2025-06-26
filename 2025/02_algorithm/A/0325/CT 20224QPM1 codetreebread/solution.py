'''
제출횟수 : 1회
풀이시간 : 1시간 10분

[ 헷갈렸던 것 ]
* 앞을 못지난다는게 무슨말이야?
* 하나의 베이스캠프에서 여러명 출발 못하나?
* 이동이 다 마치고 지나갈 수 없어진다는게,
    그 칸에 사람이 있을 수 있지만 새로 들어오진 못한다는거지?
* 사람의 이동 순서가 중요한가?

[ 시간 복잡도 ]
M*(N^2*N^2)

구상 : 9분
* bfs 두번 쓰니가 하나로 꺼내야지~
* 2차원 배열엔 막혀있는지 아닌지만 표시하면되겠네
* 사람 배열 만들어서 지금 움직여야하는 사람만 들고다니면 되겠네

구현 : 43분
* 구현 과정에서 bfs를 합치기 위해서는 base를 set으로 관리하는게 좋다고 생각하여 바꿈
* 구현 과정에서 gotobase 함수 검증하고 넘어가다가 bfs 뜯어고쳐야해서 오래걸림
* bfs 로직을 익숙치 않은대로 짜려다가 문제가 생겨서 다시 짬

디버깅 및 검증 : 22분
* 코드 흐름 보기 -> 테케 만들기 -> 코드 디테일보기 -> 새로운 화면(제출창)에서 다시보기
* 테케를 잘못 만들어서 잠시 혼란을,,,,
* 마지막에 사람이 뒤에서부터 이동되게 되어있길래,, 상관 없지만 찜찜해서 앞에서 부터로 바꿈


[테스트 케이스]
3 1
1 1 1
1 0 1
1 1 1
2 2

5 5
1 0 0 0 0
1 0 0 1 0
0 1 1 0 0
0 0 0 0 0
0 0 0 0 0
3 1
2 2
2 3
3 4
4 1

'''


from collections import deque

# bfs
# 목적지를 set으로 받아서 두 종류 bfs를 한 번에 처리
# 우선순위도 두 경우가 달라서 모든 후보를 list에 담아서 return하고 후처리
def bfs(sx, sy, end):
    q = deque()
    visited = [[0]*N for _ in range(N)]

    # q에는 시작한 방향, x, y를 넣는데,
    # 제일 처음의 경우 우선 -1로 넣고
    # 한 번 돌면서 시작 방향을 정하도록함
    q.append((-1, sx, sy))
    visited[sx][sy]=1

    candidate = []
    while q:
        nq = deque()
        while q:
            sd, x, y = q.popleft()
            if (x, y) in end:
                candidate.append((sd, x, y))

            if candidate: continue

            for d in range(4):
                # dxdy를 상좌우하 순으로 돌려서
                # 이동할 때에는 정렬을 안해도 되게 함
                dx, dy = dxdy[d]
                nx, ny = x+dx, y+dy

                if not(0<=nx<N and 0<=ny<N): continue
                # visited는 이번 턴의 방문, block은 갈 수 없는 길
                if visited[nx][ny] or block[nx][ny]: continue

                visited[nx][ny]=1
                # 제일 처음에는 d를 넣고,
                # 그 외에는 이전에 오던 처음 방향(sd)를 넣음
                if sd==-1:
                    nq.append((d, nx, ny))
                else:
                    nq.append((sd, nx, ny))

        if candidate:
            return candidate

        q = nq

def move():
    global cnt
    # 목적지에 도착한 사람의 인덱스와 목적지를 저장
    stack = []

    # 번호가 빠른 순서대로 돌면서
    for i in range(len(people)):

        idx, x, y = people[i]
        ex, ey = goal[idx]

        candidate = bfs(x, y, {(ex, ey)})

        # bfs를 상좌우하 순으로 돌기 때문에
        # 제일 앞의 것이 우선순위가 높은 것
        nd = candidate[0][0]

        dx, dy = dxdy[nd]
        x, y = x+dx, y+dy

        # 이동하고 목적지에 도착하면 stack에 저장하고
        # 종료 조건을 확인하기 위한 cnt를 1 올림
        if x==ex and y==ey:
            stack.append((i, ex, ey))
            cnt += 1
        else :
            # 아직 목적지가 아니면 좌표 업데이트
            people[i]=(idx, x, y)

    # 이번에 목적지에 도착한 경우 그 사람 없애고, 접근 불가 처리
    while stack:
        i, x, y = stack.pop()
        del people[i]
        block[x][y]=1

# 해당 시간의 사람을 basecamp로 넣기
def gotobase(time):

    ex, ey = goal[time]
    candidate = bfs(ex, ey, base)

    # 행, 열이 빠른 순으로 정렬해서 첫번째 것 사용
    candidate.sort(key = lambda x: (x[1], x[2]))
    d, x, y = candidate[0]

    # 몇번째 사람이 어느 좌표에 들어가는지 넣고, 그 배이스캠프 블락
    people.append((time, x, y))
    block[x][y] = 1

N, M = map(int, input().split())
bcdata = [list(map(int, input().split())) for _ in range(N)]
block = [[0]*N for _ in range(N)]
dxdy = ((-1, 0), (0, -1), (0, 1), (1, 0))

# bfs함수 하나 재활용을 위해 set으로 관리
base = set()
for i in range(N):
    for j in range(N):
        if bcdata[i][j]:
            base.add((i, j))

# 사람의 인덱스는 (시간이므로) 1번부터
goal = [0]+[tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
people = []

time = 0
cnt = 0

# cnt==M이 되면( 모든 사람이 목적지에 도달하면) 종료
while cnt<M:

    # 1초 늘어나고
    time += 1

    # 판 위의 사람 움직이고
    move()

    # 아직 판에 못들어온 사람 있으면,
    # 가까운 베이스캠프 찾아서 넣어주고
    if time<=M:
        gotobase(time)

print(time)

