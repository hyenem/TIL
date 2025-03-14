'''
제출 횟수 : 5회
풀이시간 : 85분


'''

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
    toperson = 0
    # 도착한 자리에 바로 사람있으면
    # 그 사람 태우기
    if arr[tx][ty] > 1:
        canperson = 1
        sx, sy, ex, ey = person[arr[tx][ty]]

        # 이거 한줄 누락한걸 못찾아서 50분을 쓰냐,,,,,,,
        # 머리 154813200대 딱콩,,,,
        arr[sx][sy]=0
    else:
        # 그 외의 경우
        # bfs 돌면서 가까운 사람 찾기
        visited = [[0] * N for _ in range(N)]
        q = deque([(tx, ty)])
        visited[tx][ty] = 1
        while q:
            toperson += 1
            nq = deque()
            candidate = []
            while q:
                x, y = q.popleft()
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < N and 0 <= ny < N): continue
                    if visited[nx][ny]: continue
                    if arr[nx][ny] == 1: continue
                    visited[nx][ny] = 1
                    if arr[nx][ny] == 0:
                        nq.append((nx, ny))
                    else:
                        candidate.append((nx, ny))

            # 이번 턴에 사람 한명이라도 있었으면
            # 그 사람들중 가장 위에 왼쪽에 있는 사람 찾기
            if candidate:
                candidate.sort()
                sx, sy, ex, ey = person[arr[candidate[0][0]][candidate[0][1]]]
                arr[sx][sy] = 0
                canperson = 1
                break

            # 사람 한명도 없으면 다음 턴
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