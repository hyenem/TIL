''' 2회독
제출횟수 : 1회
풀이시간 : 15분

* 7번이나 냈었네,,, 도대체 이걸 왜 어렵게 풀었던거지?!?!
* 시초났었어서 백준에도 다시 제출해봤는데 문제가 없음!
* 시초났었어서 백준에도 다시 제출해봤는데 문제가 없음!
* 크게 피드백 할 것 없음

[checklist]
1. 공통
[V] 0/1-based입출력 모두 확인할 것
[V] 하드코딩 한 부분 다시 검증하기
[V] 복붙 한 부분 인덱스 다 잘 수정했나
[V] while문 종료 되나
[V] 지정한 인덱스가 내가 지정하고자 한 인덱스가 맞나
[V] 정말정말정말로 빠트린 조건 없나

2. 백트래킹
[V] 재귀 종료조건 잘 설정되었나
[V] 과도한 가지치기가 되지는 않았나
[V] 모든 요소 원복 잘 해주었나
'''

def go():
    lst = [i for i in range(N)]
    for i in range(H):
        for j in range(N-1):
            if line[i][j]:
                lst[j], lst[j+1]=lst[j+1], lst[j]

    for i in range(N):
        if lst[i]!=i:
            return 0
    return 1

def btk(idx, cnt):
    global ans
    if cnt>=ans: return

    if go():
        ans = cnt
        return

    for i in range(idx+1, (N-1)*H):
        x, y = i//(N-1), i%(N-1)
        if line[x][y]: continue
        if y!=0 and line[x][y-1]: continue
        if y!=N-2 and line[x][y+1]: continue
        line[x][y]=1
        btk(i, cnt+1)
        line[x][y]=0

N, M, H = map(int, input().split())
line = [[0]*(N-1) for _ in range(H)]
data = [list(map(int, input().split())) for _ in range(M)]
for x, y in data:
    line[x-1][y-1]=1

ans = 4
btk(-1, 0)
if ans==4: ans = -1
print(ans)


''' 1회독
제출횟수 : 7회(시간초과 3회 + 틀렸습니다 3회)
    * 첫번쨰 제출 : 순열 + 다 만들고 다 내려가보기
                    당연히 시간초과
    * 두번째 제출 : 조합 + 다 만들고 다 내려가보기
                    swap으로 매번 내려가봐서 시간 초과
    * 3~5번째 제출 : 백트레킹 시작 인덱스 잘못 설정 틀렸습니다
    * 6번째 제출 : 조합 + 다 만들고 내려가보기 + 가지치기
                    시간초과
    * 7번째 제출 : 내려가면서 미리 swap해두기 -> 성공
풀이시간 : 66분

!! 명심할 것 !!
>> 조합이라고 생각하고 멍청하게 순열을 만들어둔 것은 아닌지 확인해볼것
>> 재귀 호출횟수만 고려할게 아니라 안에서 몇번도는지까지도 계산해봐야함
>> 틀린 코드에서 하나 고치고 맞는 코드라고 확신하지 말것

구상 : 8분
* 처음엔 마지막 상황을 보고 바꿔주면 될거라고 생각했는데
* 마지막줄에 항상 사다리를 놓을 수 있는게 아니라사 브루트 포스 해야한다고 생각함
* 모든 사다리에 대해서 조합을 하면 되겠다고 생각함. 어차피 3개 넘어가면 그만하니까

구현 : 14분
디버깅 : 44분
[1] 인덱스를 잘못 파악함
M과 H를 바꿔서 생각해서 인덱스 수정을 한참함
[2] 위의 틀렸습니다, 시간초과 흐름에 따라 수정,,,

리팩토링
dfs 그냥 돌려버리니까 cnt가 작은 것 부터 보는게 아니라
깊이를 쭈우욱들어갓다나와서 비효율적이됨
그래서 cnt가 1인것부터 차근히 올리도록함


def btk(cnt, bx, by):
    global ans

    if cnt == goal:
        for j in range(1, N + 1):
            res = j
            for i in range(1, H + 1):
                res = res + move[i][res]
            if res != j:
                return False
        return True

    for j in range(by + 1, N):
        if move[bx][j] or move[bx][j + 1]: continue

        move[bx][j], move[bx][j + 1] = 1, -1
        if btk(cnt + 1, bx, j):
            return True
        move[bx][j], move[bx][j + 1] = 0, 0

    for i in range(bx + 1, 1 + H):
        for j in range(1, N):
            if move[i][j] or move[i][j + 1]: continue

            move[i][j], move[i][j + 1] = 1, -1
            if btk(cnt + 1, i, j):
                return True
            move[i][j], move[i][j + 1] = 0, 0

    return False


N, M, H = map(int, input().split())
ladder = [tuple(map(int, input().split())) for _ in range(M)]
move = [[0] * (N + 2) for _ in range(H + 1)]
visited = [[0] * (N + 2) for _ in range(H + 1)]

# 사다리 표시
for x, y in ladder:
    move[x][y] = 1
    move[x][y + 1] = -1

for goal in range(4):
    if btk(0, 1, 0):
        ans = goal
        break
else:
    ans = -1

print(ans)
'''