'''
제출횟수 : 3회
풀이시간 : 29분

* arr[i][j]랑 같은걸로 비교해야하는데 arr[x][y]랑 같은거로 비교
    -> 이렇게 되면 빨강 블럭이랑 연결된 같은 색깔 블럭은 연결을 못함
* 빨강 블럭 큰게 우선순위 큰거로 착각함
* 이 문제는 반성 좀 해야겠다,,,,,, 뇌 빼고풀지말자 문제
'''

def fall():
    for j in range(N):
        acc = 0
        for i in range(N-1, -1, -1):
            if arr[i][j]==-2:
                acc+=1
            elif arr[i][j]==-1:
                acc = 0
            else:
                arr[i][j], arr[i+acc][j] = arr[i+acc][j], arr[i][j]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))

ans = 0
while True:
    visited = [[0]*N for _ in range(N)]
    cnt, rcnt = -1, -1
    loc = []
    for i in range(N-1, -1, -1):
        for j in range(N):
            if visited[i][j]: continue
            if arr[i][j] in {0, -1, -2}: continue

            visited[i][j]=1
            q = [(i, j)]
            idx = 0
            red = set()

            while idx<len(q):
                x, y = q[idx]
                idx += 1

                for dx, dy in dxdy:
                    nx, ny = x+dx, y+dy
                    if not(0<=nx<N and 0<=ny<N): continue
                    if arr[nx][ny]==0:
                        if (nx, ny) in red: continue
                        red.add((nx, ny))
                        q.append((nx, ny))
                    elif arr[nx][ny]==arr[i][j]:
                        if visited[nx][ny]: continue
                        visited[nx][ny]=1
                        q.append((nx, ny))

            if len(q)==1: continue
            if cnt<len(q):
                cnt, rcnt, loc = len(q), len(red), q
            elif cnt==len(q) and rcnt>len(red):
                rcnt, loc = len(red), q

    if len(loc)==0:
        break

    ans += (len(loc))**2
    for x, y in loc:
        arr[x][y]=-2

    fall()

    arr = list(map(list, zip(*arr)))[::-1]
    fall()

print(ans)

'''
제출횟수 : 3회
풀이시간 : 65분

실행시간 : 152ms
메모리 : 112016KB

                        !! 명심할 것 !!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!문제 꼼꼼히 읽기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
무지개 많이 나온 블럭부터 1순위라는 거를 못봐가지고 30분을 헤매는 건 좀 아니지 않니

 ____                              __
/\  _`\                           /\ \__
\ \ \L\ \   __      _ __     __   \ \ ,_\    ___
 \ \ ,__/ /'__`\   /\`'__\ /'__`\  \ \ \/   / __`\
  \ \ \/ /\ \L\.\_ \ \ \/ /\  __/   \ \ \_ /\ \L\ \
   \ \_\ \ \__/.\_\ \ \_\ \ \____\   \ \__\\ \____/
    \/_/  \/__/\/_/  \/_/  \/____/    \/__/ \/___/

파레토의 법칙을 잊지말자 : 오류의 80퍼센트는 20퍼센트에서
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
처음 문제에서 누락한 조건이나, 디버깅하면서 수정한 것들은
전체 흐름에서 짠게 아니라 추가한 거기 때문에 거기서 문제가 너무많이 발생
뭔가 추가했거나 수정했다면 그부분 최소 다섯번은 다시 확인하기



구상 : 4분
* 블럭의 종류와 상황을 이해하는데 시간을 오래 썼음
* 무지개블럭은 여러 블럭에서 동시에 사용할 수 있어서 조심히 처리해야겠다고 생각함
* 기준 블럭은 왼쪽 위니까 그냥 i, j 순으로 for문 돌면서 visited 처리 안된애들부터 시작하면
* 무지개 블럭만으로 이루어진 블럭도 없고, 기준블럭도 바로 결정 되겠다고 생각함
* 행, 열이 큰순으로 우선순위이므로 블럭의 사이즈가 같으면 계속 덮어씌워주면 되겠다고 판단

구현 : 16분
* 우선 구현을 하고, 답을 출력하기 전에 배열 찍어보면서
* 중력과 회전이 잘 적용되는지 살펴봄 -> 안돼서 바로 디버깅 시작

디버깅 : 44분
[1] 중력 로직 수정
    * 아래에서 위로 올라가면서 -2 만나면 한 줄만 swap하게 되어있었음 -> 위에 있는 애들이 끝까지 못떨어짐
    * 그래서 위에서 내려가면서 swap하게 했는데 이 경우 블럭 두개가 붙어서 내려가는 경우 처리 불가
    * 그래서 위에서 내려가면서 -2나 -1을 만날 때 까지 위로 쭈우우욱타고 올라가면서 swap하게 함
[2] 예제 2번 틀림 -> 블럭 우선순위 로직
    * 무지개 블럭이 많은게 1번 우선순위인 것을 몰랐음
    * 손으로 예제 2번을 아무리 해봐도 틀린게 없다가,,,,, 허거덩 내생각이랑 다른 블럭이 터지나? 싶어서 문제 다시읽어봄
    * 누락한 조건 확인하고 마침 무지개 블럭을 rainbow로 관리를 했어서 len(rainbow)로 조건 추가
    * 예제 2번 맞아서 제출 -> 틀렸습니다
[3] 히든 테케
    * rainbow 만들었는데 틀렸습니다 나와서 유심히 봤더니 rainbow가 같을 때에도 업데이트를 해줘야하는데 그렇지 않았음
    * 수정하고 제출 -> 틀렸습니다
    * 다시 보니까 바보같이 rainbowcnt를 업데이트 자체를 안해줌 ㅋㅋㅋ쿠ㅠㅜㅠㅜ 걍 계속 0이랑 비교한거임 ㅠㅠㅜㅠㅜㅠ
    * block 업데이트 해주면서 rainbowcnt 업데이트 되도록 로직 수정 -> 맞았습니다

[ 시간 복잡도 ]
계속 2개씩 터지면 N^2//2번까지 터질 수 있음
턴수 * (bfs에서 확인 + 떨어지기 + 돌리기 + 떨어지기)
(N*N//2)*(5N^2)-> O(N^4)
N 최대 20이므로 가능가능

[ 엣지 케이스 ] : 블럭수도 같고, 무지개 블럭 수도 같은데 기준 블럭에 따라 달라지는 경우
3 2
2 0 0
1 0 0
1 -1 2
정답 : 36
오답 : 40


def gravity():
    for i in range(1, N):
        for j in range(N):
            # 위에서 부터 내려가면서
            # -2 만나면 내 위로 -1 나오기 전가지 계속 swap하면서 올라가기
            if arr[i][j]==-2:
                for k in range(i, 0, -1):
                    if arr[k-1][j]==-1: break
                    arr[k][j], arr[k-1][j]=arr[k-1][j], arr[k][j]

# 90도 회전
def turn():
    tmp = [ele[:] for ele in arr]
    for i in range(N):
        for j in range(N):
            arr[i][j]=tmp[j][N-1-i]

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:

    # 최대 블록 찾기
    block = []
    visited = [[0]*N for _ in range(N)]
    rcnt = 0
    for i in range(N):
        for j in range(N):
            # 기준 블럭에서 부터 시작
            # 무지개 블럭으로만 이루어질 수 없으므로 숫자 블럭에서 시작하면됨
            if arr[i][j]<1: continue
            if visited[i][j]: continue

            # 인접한 블럭 중에서 무지개블럭이거나 나랑 같은거 보고 갈건데
            # rainbow는 여기저기서 들를 수 있으니까 임시set으로 관리
            q = [(i, j)]
            idx = 0
            visited[i][j]=1
            rainbow = set()

            while idx<len(q):
                x, y = q[idx]
                idx +=1
                for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                    nx, ny = x+dx, y+dy
                    if not(0<=nx<N and 0<=ny<N): continue
                    if visited[nx][ny]: continue
                    if arr[nx][ny]==0:
                        if (nx, ny) in rainbow: continue
                        q.append((nx, ny))
                        rainbow.add((nx,ny))
                    elif arr[nx][ny]==arr[i][j]:
                        visited[nx][ny]=1
                        q.append((nx, ny))

            # 머리 3498457대 때리기
            # 무지개 블럭 많은순인거 못읽어서 디버깅 오백년
            # rcnt<len(rainbow)라고 해서 틀렸습니다 1회
            # rcnt=len(rainbow)업데이트 안해서 틀렸습니다 1회

            # 블럭수가 더 많으면 업데이트
            if len(block)<len(q):
                block = q
                rcnt = len(rainbow)
            #같으면, rainbow 개수 보고, 크거나 같은 경우
            # 내가 무조건 이전보다 기준 블럭이 더 크니가 업데이트
            elif len(block)==len(q):
                if rcnt<=len(rainbow):
                    block=q
                    rcnt = len(rainbow)

    # 1짜리는 해당되지 않아요
    if len(block)<=1: break

    # 점수추가하고 빈칸 만들기
    ans += (len(block))**2
    while block:
        x, y = block.pop()
        arr[x][y]=-2

    gravity()
    turn()
    gravity()

print(ans)
'''