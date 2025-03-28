'''
제출횟수 : 1회
풀이시간 : 1시간 8분

[ 오해할 만한 점 ]
* maze가 회전할 때 사람이랑 출구도 회전할거라고 생각을 못함
* 한 칸에 여러명이 동시에 있을 수 있나?

구상 : 8분
* 문제 조건들 정리
* 움직이는 로직 if문으로 어떻게 처리할 지,
* 정사각형의 변 어떻게 계산할 지 등을 결정

구현 : 28분
* 함수별로 검증하면서 넘어감

디버깅 및 검증 : 32분
[ openTC ]
* 회전 범위가 이상하게 잡힘
    -> 기존 배열 복사하고 참조해서 바꿔줘야하는데, 그냥 원본 배열에서 돌림;;
    -> size를 두 점의 좌표 차이 +1로 잡아줘야하는데 +1 인했음
* 상하 좌우 우선순위 잘못 잡음
* 좌우로 이동할 때 nx=rx로 설정해야하는데 nx = ex로 설정함
* exit 좌표 출력을 0base로 함

[ 이후 ]
* 코드 다시 보기
    -> 정사각형 시작 점을
    sx, sy = min(sx, tmpsx), min(sy, tmpsy)
    이렇게 처리했는데
    이러면 아예 불가능한 점이 기준점으로 잡혀버릴 수 있음
    sx, sy = min((sx, sy), (tmpsx, tmpsy))로 수정


[ 시간 복잡도 ]
K*(M+N*N)

[ 테스트 케이스 ]
1. move() 함수 만들고 잘 이동하는지 채크
5 3 8
0 0 0 0 1
9 2 0 0 0
0 0 0 0 0
0 0 0 1 0
0 0 0 0 0
1 4
3 1
3 5
3 3

2. rotate() 채크
5 1 100
10 10 10 10 10
10 2 0 4 10
10 5 6 7 10
10 8 9 0 10
10 10 10 10 10
2 3
4 4


'''


def move():
    global move_cnt

    for i in range(len(runner) - 1, -1, -1):  # 뒤에서 부터 보는 이유는
        rx, ry = runner[i]  # 탈출한 애들 인덱스 안깨지게
        if exit_x != rx:  # 상하부터 이동
            ny = ry
            if exit_x > rx:
                nx = rx + 1  # 목표지점이 더 위에있으면 위로
            else:
                nx = rx - 1  # 더 아래있으면 아래로
            # 갈 수 있으면 가기
            if 0 <= nx < N and 0 <= ny < N and not maze[nx][ny]:
                move_cnt += 1  # 이동 횟수 늘리기
                if (nx, ny) == (exit_x, exit_y):
                    del runner[i]
                else:
                    runner[i] = (nx, ny)
                continue

        if ry != exit_y:  # 상하로 안움직였을 경우
            nx = rx
            if exit_y > ry:
                ny = ry + 1  # 목표지점이 오른쪽에 있으면 오른쪽으로
            else:
                ny = ry - 1  # 왼쪽에 있으면 왼쪽으로
            # 갈 수 있으면 가기
            if 0 <= nx < N and 0 <= ny < N and not maze[nx][ny]:
                move_cnt += 1  # 이동 횟수 늘리기
                if (nx, ny) == (exit_x, exit_y):
                    del runner[i]
                else:
                    runner[i] = (nx, ny)


def rotate():
    global exit_x, exit_y

    # 작은 사이즈를 만들 수 있는 사람들의 좌표를 저장
    candidate = []
    size = N + 1
    for i in range(len(runner)):
        rx, ry = runner[i]

        # 해당 사람을 포함하는 정사각형의 사이즈는
        # 사람과 탈출구를 마주보는 꼭짓점으로 하는 직사각형 중 큰 변입니다
        # 따라서 x좌표 차, y좌표 차 중 큰 것을 가져가면 됩니다
        tmpsize = max(abs(exit_x - rx), abs(exit_y - ry)) + 1

        # 기존 저장되어있던 사이즈보다 작으면 후보 다 없어지고 나만남기
        # 같으면 나만 후보에 추가
        if size > tmpsize:
            candidate.clear()
            candidate.append((rx, ry))
            size = tmpsize
        elif size == tmpsize:
            candidate.append((rx, ry))

    sx, sy = N + 1, N + 1  # 정사각형의 시작점입니다
    for rx, ry in candidate:
        ex, ey = max(rx, exit_x), max(ry, exit_y)  # 직사각형의 끝점입니다(정사각형x)

        tmpsx, tmpsy = max(0, ex - size + 1), max(0, ey - size + 1)  # 직사각형의 끝 점에서 가능한 왼쪽, 위쪽으로 올라가서
        # 정사각형의 시작점을 잡습니다.
        sx, sy = min((sx, sy), (tmpsx, tmpsy))  # 시작점이 가능한 작은 점이 시작점이 됩니다

    # 탈출구와 회전위 사람 좌표 변환
    # 기존 좌표의 sx, sy 기반 상대 좌표를 찾은 뒤, 90도 회전시키고
    # 다시 sx, sy 에 대하여 그만큼 옮겨줍니다
    exit_x, exit_y = sx + (exit_y - sy), sy + (size - 1 - (exit_x - sx))

    for i in range(len(runner)):
        rx, ry = runner[i]
        if 0 <= rx - sx < size and 0 <= ry - sy < size:  # 회전하는 범위 내이면,
            runner[i] = sx + (ry - sy), sy + (size - 1 - (rx - sx))  # 회전해주기

    # 좌표를 기반으로 장애물들 회전
    tmpmaze = [ele[:] for ele in maze]
    for i in range(size):
        for j in range(size):
            maze[sx + i][sy + j] = max(0, tmpmaze[sx + size - 1 - j][sy + i] - 1)


N, M, K = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
runner = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
exit_x, exit_y = map(lambda x: int(x) - 1, input().split())

move_cnt = 0

for _ in range(K):

    move()  # 이동하기

    # 사람 한 명도 안남으면 그만합니다
    if len(runner) == 0: break

    rotate()  # 회전하기

print(move_cnt)
print(exit_x + 1, exit_y + 1)  # 0-based로 바꿔서 다시 원복
