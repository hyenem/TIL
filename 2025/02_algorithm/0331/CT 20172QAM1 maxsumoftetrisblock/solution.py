''' 2회독
제출횟수 : 2회
풀이시간 : 7분

* 최근에 풀어본 문제라고 문제를 파악을 안하고 그냥 손가는대로 풀었다
    -> 틀렸습니다의 원인
    -> 그냥 한 줄로 쭉간는 경우만 함,,,,ㅋㅅㅋ,,,,
* 처음 보는 느낌으로 풀 것

* 코드는 변수명만 다르고 그냥 똑같음
* 예전에는 리팩토링으로 했던 것까지 한 번에 구현함

[ 채크리스트 ]
[V] 하드코딩 한 부분 다시 검증하기(해당없음)
[V] 복붙 한 부분 인덱스 다 잘 수정했나(해당없음)
[V] while문 종료 되나(해당없음)
[V] 재귀 종료조건 잘 설정되었나
[V] 과도한 가지치기가 되지는 않았나
'''

def btk(acc):
    global ans

    if acc + (4-len(root))*maximum<= ans:
        return

    if len(root)==4:
        ans = acc
        return

    for x, y in root:
        for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<M) or visited[nx][ny]: continue
            visited[nx][ny]=1
            root.append((nx, ny))
            btk(acc+arr[nx][ny])
            visited[nx][ny]=0
            root.pop()

N, M = map(int, input().split())
arr= [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

maximum = max(map(max, arr))

ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]: continue
        visited[i][j]=1
        root = [(i, j)]
        btk(arr[i][j])

print(ans)

'''1회독
제출횟수 : 1회
풀이시간 : 12분

실행시간 : 648ms
메모리 : 115468KB
코드길이 : 780B

명심할 것!
* 함수 쓸때 매개변수 무지성 0 넣기 금지. 뭘 쓰든 생각을 하고 쓸것,,
* 백트래킹할 때 변화시킨 것들 다 보고 백할 것들에 대해 채크해보기
  특히 처음 함수 불러올 때 더더욱 조심할 것

[1] 구상 : 4분
* 이전에 풀어봤던 문제라 문제를 읽는데 오래 걸리지 않았음
* 테트로미노는 정사각형을 어떻게든 4개 연결하면 되기 때문에
* 재귀로 가면서 연결되어있는 블럭의 네방향을 모두 추가하면 되겠다고 판단
* 최근에 풀이한 ''소문난 칠공주'' 문제가 생각났음
* 시간복잡도를 조금 우려함
    * 첫번째 블럭에 대해서는 모든 방향을 다 보고 다음으로 넘어가니까
    * 방문 표시를 없애줄 필요가 없음
    * 그러면 왼쪽과 위가 다 방문표시가 되어있는 상태에서
    * 배치할 수 있는 테트로미노는 대강 16가지 정도 됨
    * (백준 기준) 500*500*16 이고, 시간 제한이 2초이므로 가능

[2] 구현 : 8분
* 처음에 블럭이 들어있는 배열을 매개변수로 들고다니려다가 그럴 필요가 없어서 수정
* 반복문을 돌면서 시작하는 블럭의 visited는 다시 false로 만들 필요가 없지만
  block은 사용한 뒤에 꺼내줬어야만하는데, 이걸 안꺼내줘서 무한 루프가 돌았음
    * block 출력해보고 확인하고 바로 해결함
* 처음에 acc에 시작 블럭의 수를 넣고 돌렸어야하는데 0으로 돌려서 답이 안나옴
* 혹시 몰라서 500*500을 1로 채워보고 시간 채크

[3] 리펙토링
* visited를 0, 1로 표시하도록 생성했는데,
* 재귀안에서 True, False로 처리함,,, 물론 답이 나오는데 상관은 없었지만,,,(파이썬 땡큐)
* 0, 1 로 처리하도록 수정함


def solution(acc):
    global ans
    if acc+mx*(4-len(block))<=ans: return

    # 블럭이 4개가 되면 최댓값 찾기
    if len(block)==4:
        ans = max(ans, acc)
        return
    # 지금까지 봤던 블럭들 중 하나를 골라서
    # 네 방향 중 하나를 골라서 감
    for x, y in block:
        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if not (0<=nx<N and 0<=ny<M): continue
            if visited[nx][ny]: continue
            visited[nx][ny]=1
            block.append((nx, ny))
            solution(acc+arr[nx][ny])
            block.pop()
            visited[nx][ny]=0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dxdy = ((0, -1), (0, 1), (1, 0), (-1, 0))
block = []
mx = max(map(max,arr))
ans = 0
for i in range(N):
    for j in range(M):
        visited[i][j]=1
        block.append((i,j))
        solution(arr[i][j])
        block.pop()
print(ans)
'''