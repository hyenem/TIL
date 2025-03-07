'''
[주요 스킬]
* queue 구현
* 점수 미리 계산해두기
* 주사위 굴리기 방법

[테스트케이스]
* testcase
2 2 100
1 1
1 1
점수계산을 매번 해주는데
방문 표시를 리셋 안해주면 문제가 발생할지도

[시간복잡도]
O(NM+K)

[잘못 읽을 수 있는 것]
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

'''

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