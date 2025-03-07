'''
제출횟수 : 1회
풀이시간 : 31분

실행시간 : 116ms
메모리 : 113496KB

! 명심할 것 !
어이xxxxxxxxx 문제
뱀의 몸 길이는 변하지 않는다면서,,, 머리가 길어질 때 일단 꼬리는 유지,,,
>> 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
>> 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
>> 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    ** 먼저 ** 라는 한 단어가 이렇게 큰 영향을 미칠줄이야
    일단 몸 늘리고 자기 몸과 부딪히면 게임 끝남
>> 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
>> 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
(오해한 코드) 별표친 부분 위치가 다름
    time += 1
    hx += dxdy[d][0]
    hy += dxdy[d][1]
    snaketail.append((hx, hy))

    if not(0<=hx<N and 0<=hy<N): break

    if mapp[hx][hy]!=2:
        mapp[tx][ty]=0
        tx, ty = snaketail.popleft()

    # 꼬리 처리 먼저하고 게임 끝 처리하려함
    **if mapp[hx][hy]==1: break**

    mapp[hx][hy]=1

구상 : 5분
* 사과, 뱀을 어떻게 관리할지 고민
* 사과랑 뱀의 현재 위치를 동시에 관리해도 문제가 안생김
* 뱀이 지나가는 순간 사과는 없어지기 때문
* 뱀, 사과 위치를 2차원 배열로 관리하고,
* 뱀이 지나온 길을 보관해야 꼬리가 이동할 수 있으니까 덱으로 관리하고,
* 머리좌표, 꼬리좌표 관리하자

구현 : 17분
* 방향 전환을 어떻게 관리할지 생각을 안하고 넘어감
* 방향을 배열로 관리하고, 다음 전환할 명령을 idx로 관리

디버깅 : 9분
* 뱀 이동하는 것 하나씩 찍어보면서 왜 테케 안나오는지 확인함
* 뱀은 너무 잘 움직였고,,,,,, 테케 답이 틀렸다고 생각했지만,,,
* 꼬리 안줄이고 머리 늘렸을때 끝나게하면 테케의 답이 맞아서 문제 이해 다시함

* idx가 L이상일때 if문을 돌떄 index 에러가 나서
* idx<L 조건 추가

[시간복잡도]
방향 다 돌고 N번 지나면 벽이랑 부딪히겠지
대강 (max(X)+N)의 상수배(10000이 X의 최댓값)

[테스트케이스] : 꼬리 먼저 이동하면xxx
10
3
1 2
2 1
2 2
4
1 D
2 D
3 D
4 D
'''

from collections import deque

N = int(input())
# 뱀이 간 길을 기억하기 위해서 뱀의 꼬리가 될 후보들을 q에 저장
snaketail = deque()

# mapp에 뱀의 위치와 사과의 위치를 기록
mapp = [[0]*N for _ in range(N)]
mapp[0][0]=1

# 뱀의 머리와 꼬리의 좌표
hx, hy = 0, 0
tx, ty = 0, 0
dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 사과 푶시
for _ in range(int(input())):
    ax, ay = map(lambda x: int(x)-1, input().split())
    mapp[ax][ay]=2

L = int(input())
switch = [tuple(input().split()) for _ in range(L)]
# 다음으로 만날 방향 전환 인덱스
idx = 0

time = 0
d = 0
while True:
    time += 1
    hx += dxdy[d][0]
    hy += dxdy[d][1]
    # 뱀이 진행하는 길을 꼬리의 후보에 저장
    snaketail.append((hx, hy))

    # 충격실화,, 꼬리 이동 전에 꼬리랑 머리랑 부딪히면 끝난다,,,
    if not(0<=hx<N and 0<=hy<N): break
    if mapp[hx][hy]==1: break

    # 사과가 아니면 꼬리칸 0 만들고,
    # 꼬리 한 칸 전진
    if mapp[hx][hy]!=2:
        mapp[tx][ty]=0
        tx, ty = snaketail.popleft()

    # 머리 1 표시
    mapp[hx][hy]=1

    # 방향 전환
    if idx<L and time==int(switch[idx][0]):
        if switch[idx][1]=='D':
            d = (d+1)%4
        else :
            d = (d+3)%4
        idx += 1

print(time)