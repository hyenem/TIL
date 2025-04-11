'''
제출횟수 : 2회
풀이시간 : 22분

* 판 바깥으로 나갔을 때 d바꾸고 dx, dy 갱신 안해줘서 틀렸습니다 1회
* 확실히 이제 주사위 굴리는건 깔꼼하게 잘하네~
'''

cube = [1, 2, 3, 4, 5, 6]
roll = [(3, 1, 0, 5, 4, 2),
        (4, 0, 2, 3, 5, 1),
        (2, 1, 5, 0, 4, 3),
        (1, 5, 2, 3, 0, 4)]
N, M = map(int, input().split())
arr= [list(map(int, input().split())) for _ in range(N)]
dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0))
score = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if score[i][j]: continue

        q = [(i, j)]
        idx = 0
        score[i][j]=-1
        while idx<len(q):
            x, y = q[idx]
            idx += 1
            for dx, dy in dxdy:
                nx, ny = x+dx, y+dy
                if not(0<=nx<N and 0<=ny<N): continue
                if score[nx][ny]: continue
                if arr[nx][ny]==arr[x][y]:
                    score[nx][ny]=-1
                    q.append((nx, ny))

        for x, y in q:
            score[x][y]=len(q)*arr[x][y]

x, y, d = 0, 0, 0
ans = 0
for _ in range(M):
    dx, dy = dxdy[d]
    x, y = x+dx, y+dy
    if not(0<=x<N and 0<=y<N):
        d = (d+2)%4
        dx, dy = dxdy[d]
        x, y = x+dx*2, y+dy*2

    ans += score[x][y]

    cube = [cube[roll[d][i]] for i in range(6)]
    if cube[5]>arr[x][y]:
        d = (d+1)%4
    elif cube[5]<arr[x][y]:
        d = (d-1)%4
print(ans)

'''

잘못 읽을 수 있는 것
'''

'''
제출횟수 : 1회
풀이시간 : 34분

실행시간 : 232ms -> 100ms
메모리 : 114900KB -> 109544KB

! 명심할 점 !
* 문제를 오해하지 말고, 꼬아읽지 말고 있는 그대로 읽기
* 문제가 복잡한 경우 예제 하나는 어떻게 돌아가는지 구체적으로 확인해보기

* 오해한 점
>> 칸 (x, y)에 대한 점수는 다음과 같이 구할 수 있다.
>> (x, y)에 있는 정수를 B라고 했을때, (x, y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 C를 모두 구한다.
>> 이때 이동할 수 있는 칸에는 모두 정수 B가 있어야 한다. 여기서 점수는 B와 C를 곱한 값이다.
* 오해 : 주사위가 가는 방향 중 아래 칸의 숫자가 같은 경우가 C에 카운팅 되는 줄 알았음
        코드를 아래와 같이 짬

            for _ in range(K):
                roll()
                cnt = 1
                num = arr[x][y]
                A, B = dice[1][3], arr[x][y]
                if A > B:
                    d = (d + 1) % 4
                elif A < B:
                    d = (d + 3) % 4

                while True:
                    nx, ny = x+dxdy[d][0], y+dxdy[d][1]
                    if not(0<=nx<N and 0<=ny<M): break
                    if num != arr[nx][ny]: break
                    roll()
                    cnt += 1
                    A, B = dice[1][3], arr[x][y]
                    if A > B:
                        d = (d + 1) % 4
                    elif A < B:
                        d = (d + 3) % 4

                ans += cnt*num

* 실제 : 적힌 수가 같은 연결된 칸의 개수만큼 점수를 획득하는 것이었음


구상 : 6분
* 시키는대로 해야겠다는 생각
* 주사위를 어떻게 관리할지 고민 -> 주어진 전개도를 전치해서 관리
* 범위 벗어나면 어떻게 해지? 해서 한 번 더 읽어봄

구현 : 16분
디버깅 : 14분
* 이것 저것 쓸데 없이 수정하다가 7분 뒤 문제 잘못 읽은 걸 깨달음
* 이후 수정하여 4분동안 재구현
* 반대방향을 d = 2-d 로 처리했는데, 오류. d=(d+2)%4로 수정(3분)

리팩토링
* 처음 문제 이해한 대로 하면 주사위를 굴릴 떄 마다 점수를 계산해주어야해서,
* 문제를 다시 이해한 이후에도 굴릴 때 마다 계산하도록 짯는데
* 제출하고 보니 칸 별 점수가 바뀌지 않는 다는 것을 알게됨
* 주사위 굴리기 시작 전에 bfs 돌면서 전체 점수 계산하도록 수정

* testcase
2 2 100
1 1
1 1
점수계산을 매번 해주는데
방문 표시를 리셋 안해주면 문제가 발생할지도


def roll():
    global x, y, d
    x += dxdy[d][0]
    y += dxdy[d][1]
    # 갈 수 없는 칸이면 반대로 두개 가기
    if not (0<=x<N and 0<=y<M):
        d = (d+2)%4
        x += 2*dxdy[d][0]
        y += 2*dxdy[d][1]

    # 방향에 따라 주사위 굴리기
    if d==0:
        dice[1].insert(0, dice[1].pop())
    elif d==2:
        dice[1].append(dice[1].pop(0))
    elif d==1:
        dice[0], dice[1][1], dice[2], dice[1][3]=dice[1][3],dice[0], dice[1][1], dice[2]
    else :
        dice[0], dice[1][1], dice[2], dice[1][3] = dice[1][1], dice[2], dice[1][3], dice[0]

# 주사위 생성
dice = [2, [4, 1, 3, 6], 5]

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dxdy = ((0,1), (1, 0), (0, -1), (-1, 0))
score = [[0]*M for _ in range(N)]

# 모든 칸의 점수 미리 계산하기
for i in range(N):
    for j in range(M):
        if score[i][j]: continue
        q = [(i, j)]
        # 지금 가고 있는 길 방문표시
        score[i][j]=-1
        idx = 0
        while idx<len(q):
            x, y = q[idx]
            idx += 1
            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < N and 0 <= ny < M): continue
                if score[nx][ny]: continue
                # 이전 칸과 방향이 같은 경우에 q에 넣기
                if arr[nx][ny] == arr[i][j]:
                    score[nx][ny]=-1
                    q.append((nx, ny))

        # 점수 같은 칸들 개수
        # 해당 인접 점수들 다 채우기
        cnt = len(q)
        while q:
            x, y = q.pop()
            score[x][y] = arr[x][y]*cnt

x, y = 0, 0
d = 0
ans = 0
# K번 반복
for _ in range(K):
    # 주사위 굴리기
    roll()

    # 점수 더하기
    ans += score[x][y]

    # 방향 갱신하기
    A, B = dice[1][3], arr[x][y]
    if A > B:
        d = (d + 1) % 4
    elif A < B:
        d = (d + 3) % 4

print(ans)
'''