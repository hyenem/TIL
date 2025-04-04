''' 2회독
제출횟수 : 1회
풀이시간 : 15분

* 1회독 틀렸습니다 1회(자료형 바꾸고 함수 안바꿔서)
* 1회독은 힙큐로 2회독은 deque로 풀었음
'''

from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

rx, ry, level, eaten = -1, -1, 2, 0
for i in range(N):
    for j in range(N):
        if arr[i][j]==9:
            rx, ry = i, j
            arr[rx][ry]=0
            break
    if rx!=-1: break

ans = 0
while True:
    q = deque([(rx, ry)])
    visited = [[0]*N for _ in range(N)]
    visited[rx][ry]=1
    candidate = []
    time = 0
    while q:
        nq = deque()
        while q:
            x, y = q.popleft()
            if 0<arr[x][y]<level:
                candidate.append((x, y))

            if candidate: continue
            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nx, ny = x+dx, y+dy
                if not(0<=nx<N and 0<=ny<N): continue
                if visited[nx][ny]: continue
                if arr[nx][ny]>level: continue
                visited[nx][ny]=1
                nq.append((nx, ny))

        if candidate:
            candidate.sort()
            rx, ry = candidate[0]
            arr[rx][ry]=0
            eaten += 1
            ans += time
            if eaten==level:
                eaten=0
                level+=1
            break
        else:
            q = nq
            time += 1
    else:
        break

print(ans)

''' 1회독
제출횟수 : 2회
    * heapq 만들고 heappush가 아니라 append로 원소 추가함
풀이시간 : 46분

실행시간 : 128ms
메모리 : 111940KB


! 명심할 것 !
[1]
문제에서 순서가 지정되어있을 때
몇 단계 거쳐서 해보면서
정말 그 순서대로 도는지 확인해볼것

[2]
자료 구조 바꾸면 ctrl+f 이용해서 전체 다 수정했는지 확인해볼것


구상 : 2분30초
* bfs로 돌리면서 방향 설정 잘 해서 먹을 수 있는 상어 만나면 먹게 처리
!!!!!!!!!!!!!!!!!!! 여기서 한 개 큰 오해 !!!!!!!!!!!!!!!!!!!!!!!!
>> 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기,
>> 그러한 물고기가 여러마리라면,가장 왼쪽에 있는 물고기를 먹는다.
bfs <<상 좌 우 하>> 로 돌리면 순서대로 돌아가는 줄 알았는데, 아니었음,,,,

구현 : 10분
디버깅 : 33분
[1] 종료조건 flag 잘못 사용
    if flag -> if not flag로 변경
[2] 맵 출력해가면서 원인 분석하는데 한오백년
[3] 제출하고 멘탈 붙잡는데 한오백년
[4] q.append를 heapq.heappush 로 바꿈

[시간 복잡도]
N^4*logN
최악의 경우 160000*5 대강 800000정도?

[엣지케이스] : 무작정 bfs 위 왼쪽 오른쪽 아래 순서로 돌리면 오류나는 경우
5
0 0 0 0 0
0 0 0 0 0
0 0 9 0 1
0 1 0 0 0
0 0 0 0 0


import heapq

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

size = 2
for i in range(N):
    for j in range(N):
        if arr[i][j]==9:
            sx, sy = i, j
            arr[i][j]=0

eat = 0
time = 0

# 물고기를 먹을 수 있는 동안 반복
while True:
    q = [(0, sx, sy)]
    visited = [[0]*N for _ in range(N)]
    visited[sx][sy]=1

    # 시간, 행, 열이 작은 순으로 꺼내기
    while q:
        t, x, y = heapq.heappop(q)

        # 먹을 수 있는 물고기면 먹기
        if arr[x][y]!=0 and arr[x][y]<size:
            arr[x][y]=0
            sx, sy = x, y
            time += t
            eat+=1
            # 내 크기만큼 먹었으면
            # 먹은 개수 초기화하고 성장하기
            if eat==size:
                eat=0
                size +=1
            break

        for dx, dy in ((-1, 0), (0, -1), (0,1), (1, 0)):
            nx, ny = x+dx, y+dy
            # 못가는 길을 제외하고는 일단 넣어주기
            if not (0<=nx<N and 0<=ny<N): continue
            if visited[nx][ny]: continue
            if arr[nx][ny]>size: continue
            visited[nx][ny]=1
            heapq.heappush(q, (t+1, nx, ny))
            continue

    # 물고기를 먹고 나면 break를 하는데
    # break가 안됐다는 건 물고기를 못먹었다는 거니깐
    # 엄마상어한테 도움 요청
    else :
        break

print(time)
'''