'''2회독
제출횟수 : 3회
풀이시간 : 40분

* 도착 지점이 중복이 될 수 있다!!!!!!!!!!!!!!!!
* 정보가 특정 좌표로 주어질 때 중복가능한지 꼭 확인할 것

* 예외 처리를 따로 안해도 되는 코드라 1회독 보다 나아짐
* 다만 1회독에선 놓치지 않았던 조건을 놓친게 아쉬움
'''

from collections import deque

def gotop():
    q = deque([(tx, ty)])
    visited = [[0]*N for _ in range(N)]
    visited[tx][ty]=1
    candidate = []
    cnt = 0
    while q:
        nq = deque()
        while q:
            x, y = q.popleft()
            if start[x][y]:
                candidate.append((x, y))

            if candidate: continue
            for dx, dy in dxdy:
                nx, ny = x+dx, y+dy
                if not(0<=nx<N and 0<=ny<N) or visited[nx][ny]: continue
                if arr[nx][ny]: continue
                visited[nx][ny]=1
                nq.append((nx, ny))

        if candidate:
            nx, ny = sorted(candidate)[0]
            return nx, ny, cnt

        q = nq
        cnt += 1

    return -1, -1, -1


def gotog(p):
    q = deque([(0, tx, ty)])
    visited = [[0] * N for _ in range(N)]
    visited[tx][ty] = 1
    while q:
        cnt, x, y = q.popleft()
        if (x, y)==(pdata[p-1][2]-1, pdata[p-1][3]-1):
            return x, y, cnt

        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny]: continue
            if arr[nx][ny]: continue
            visited[nx][ny] = 1
            q.append((cnt+1, nx, ny))

    return -1, -1, -1

dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
N, M, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tx, ty = map(lambda x: int(x)-1, input().split())
pdata = [list(map(int, input().split())) for _ in range(M)]
start = [[0]*N for _ in range(N)]
for i, (sx, sy, gx, gy) in enumerate(pdata, start = 1):
    start[sx-1][sy-1]=i

for _ in range(M):
    tx, ty, cnt= gotop()
    if cnt==-1 or C<=cnt:
        print(-1)
        break

    p = start[tx][ty]
    start[tx][ty]=0
    C -= cnt

    tx, ty, cnt = gotog(p)
    if cnt==-1 or C<cnt:
        print(-1)
        break
    C += cnt
else:
    print(C)
    
    
''' 1회독
제출 횟수 : 5회
풀이시간 : 85분

실행시간 : 172ms
메모리 : 114968KB

!!!!!!!!!!!!!오늘의 다짐!!!!!!!!!!!!!!!!
그냥 엣지케이스를 예외 처리하지마.
그냥 하나의 로직으로 통합해.
엣지케이스 예외처리에서 조건 누락해서 틀리는게 너무너무 많자나.

[ 오해할 뻔한 것 ]
* 사람 있는데는 못지나가나?
* 아예 사람이나 목적지에 도달도 못하면 어카지? -> 테스트케이스가 해결해줌

[ 시간 복잡도 ]
O(M*N^4)
최대 20^6

[ 엣지 케이스 ] : 목적지에서 다음 사람까지 아예 안움직임
2 3 3
0 0
0 0
1 1
1 1 1 2
1 2 2 2
2 2 2 1
출력 : 6

구상 : 4분
* oil양이 충분한지를 매번 채크해주면 시간적으로 효율적이엤지만, 내가 힘드니가
* 사람까지 가는 거리, 사람에서 목표까지 가는 거리 다 계산 한 다움에
* 사람을 목적지까지 데려갈 수 있는지를 계산해두자

구현 : 19분
* 한 줄 틀린것빼고 완벽구현,,,,
* 구현하면서, 오,, 아예 못가는 경우도 처리해야겠네, 천재다 라고 생각했는데

디버깅 : 62분
* 지금 있는 자리에서 바로 손님을 태울 때에
* 손님을 태우고 손님을 지워야하는데,
* 해당 로직을 이동해서 손님 태울때는 써놓고, 바로 손님 태울때는 안씀
* Ha,,,,, 리팩토링 해서 그 코드를 아예 없앰

리팩토링
* 바로 줍는 것과 이동해서 줍는 로직을 통합시킴

from collections import deque


N, K, oil = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tx, ty = map(lambda x: int(x) - 1, input().split())
person = [0, 0] + [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(K)]

# 지도에 사람 표시
for i in range(2, K + 2):
    sx, sy, ex, ey = person[i]
    arr[sx][sy] = i

# K번 반복(문제에서는 M)
for _ in range(K):

    canperson = 0
    cangoal = 0

    # 다음 사람까지 가는 거리를 계산
    # bfs 돌면서 가까운 사람 찾기

    # 엣지를 if else로 구분하려니까 자꾸 실수가 생기자나
    # 그냥 통용가능한 로직으로 써
    toperson = 0
    visited = [[0] * N for _ in range(N)]
    q = deque([(tx, ty)])
    visited[tx][ty] = 1
    candidate = []
    while q:
        nq = deque()
        while q:
            x, y = q.popleft()
            if arr[x][y]>1:
                candidate.append((x, y))
                continue
            if candidate: continue

            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = x + dx, y + dy
                if not (0 <= nx < N and 0 <= ny < N): continue
                if visited[nx][ny]: continue
                if arr[nx][ny] == 1: continue
                visited[nx][ny] = 1
                nq.append((nx, ny))

        # 이번 턴에 사람 한명이라도 있었으면
        # 그 사람들중 가장 위에 왼쪽에 있는 사람 찾기
        if candidate:
            candidate.sort()
            sx, sy, ex, ey = person[arr[candidate[0][0]][candidate[0][1]]]
            arr[sx][sy] = 0
            canperson = 1
            break

        # 사람 한명도 없으면 다음 턴
        toperson += 1
        q = nq
    # 사람한테 도달 자체를 못했으면 break
    if not canperson: break


    # 목적지까지 거리 찾기
    cangoal = 0
    togoal = 0
    q = deque([(0, sx, sy)])
    visited = [[0] * N for _ in range(N)]
    visited[sx][sy] = 1
    while q:
        t, x, y = q.popleft()
        if x == ex and y == ey:
            togoal = t
            cangoal = 1
            break

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N): continue
            if visited[nx][ny]: continue
            if arr[nx][ny] == 1: continue
            visited[nx][ny] = 1
            q.append((t + 1, nx, ny))

    # 목적지까지 아예 도착을 못했으면 break
    if not cangoal: break

    # 이 손님을 태우고 목적지까지 가는데
    # 기름이 충분히 있나요?
    if oil >= toperson + togoal:
        oil = oil - toperson + togoal
        tx, ty = ex, ey
    else:
        # 없으면 못갑니다
        cangoal = 0

    if not cangoal: break

# K번 모두 손님도 태울 수 있었고, 목적지로도 갈 수 있었으면 남은 기름 출력
if cangoal and canperson:
    print(oil)
else:
    print(-1)
'''