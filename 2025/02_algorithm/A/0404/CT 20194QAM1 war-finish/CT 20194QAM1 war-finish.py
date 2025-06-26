'''2회독
제출횟수 : 1회
풀이시간 : 24분

* 백준에서는 인덱스를 일일이 줬는데 얘는 안줘서 느낌이 아예 달랐던 문제
* 나 인제 인덱스 잘 처리한다! 겁내지말고 꼼꼼하게 처리만해주면돼!!!!!!!!!!
* 풀이시간도 많이 단축됐음.
* 별다른 피드백 없음

'''

def split():
    color = [[1]*N for _ in range(N)]
    for i in range(u[0]):
        for j in range(u[1]+1):
            color[i][j]=2
        for j in range(u[1]+1, N):
            color[i][j]=3
    for i in range(d[0]+1, N):
        for j in range(d[1]):
            color[i][j]=4
        for j in range(d[1], N):
            color[i][j]=5

    for i in range(u[0], l[0]):
        for j in range(u[1]-i+u[0]):
            color[i][j]=2
    for i in range(l[0], d[0]+1):
        for j in range(l[1]+i-l[0]):
            color[i][j]=4

    for i in range(u[0], r[0]+1):
        for j in range(u[1]+1+i-u[0], N):
            color[i][j]=3
    for i in range(r[0]+1, d[0]+1):
        for j in range(r[1]-i+r[0]+1, N):
            color[i][j]=5

    ansarr = [0]*6
    for i in range(N):
        for j in range(N):
            ansarr[color[i][j]]+=arr[i][j]
    ansarr = ansarr[1:]
    return max(ansarr)-min(ansarr)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = sum(map(sum, arr))
for i in range(N):
    for j in range(N):
        u = (i, j)
        for lc in range(1, j+1):
            if i+lc>=N: break

            l = (i+lc, j-lc)
            for rc in range(1, N-j):
                if i+rc+lc>=N: break

                r = (i+rc, j+rc)
                d = (i+rc+lc, j-lc+rc)

                ans = min(ans, split())

print(ans)

'''
제출 횟수 : 2회
    * d1 조건을 잘못 걸어줘서 틀렸습니다.
풀이 시간 : 55분

실행시간 : 256ms
메모리 : 111932KB


!! 명심할 것 1 !!
스텐스를 한 가지로 유지하기,,,
>>처음 문제를 보고 했던 생각
    복잡하게 생각하지 말고 문제에서 주어진 범위대로 구현하자
>> 하지만?
    x, y 가 1이상 N이하인 걸 0이상 N미만으로 설정해버려서
    틀리기도 한 번 틀렸고, 그거 보정하는데 시간이 너무너무너무 오래걸림
주어진 부등식 이용할거면 모든걸 다 그렇게 해야지,,,,

!! 명심할 것 2 !!
제발,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, 디버깅 중에 뭔가 이상한걸 발견하면
어디다가 좀 써놓자,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
디버거 찍어보면서 0번 열부터 시작하는거 안나오는걸 이미 확인을 했잔니,,,,,,,,,,,,,,,,
그런데 왜 그냥 제출을 하는거야 혜민아,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
왜 그걸 그새 까먹는거야,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
안까먹게 좀 메모좀 하자,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
나는 머리가 그렇게까지 좋지 못하다,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,



구상 : 9분
* 문제를 읽으면서 구역이 어떻게 나뉘는지 이해가 잘 안됐음,,,,
* 그래서 예시 보면서 상황을 이해하고, 그냥 경계대로 구현하려고함,,, 이해를 포기했달까
* 근데 5번 구역 나누려고 보니까 조건문 거는게 너무 까다로움
* 반면 1, 2, 3, 4 번 구역은 하나의 규칙을 따라서 구획할 수 있으니까
* 그냥 1, 2, 3, 4번 구역 먼저 처리하고 나머지 구역 처리하자!

구현 : 28분
* 인덱스 처리가 너무 까다로워서 구현이 오래걸렸음
* 구현 하는 과정에서 디버거랑 프린트로 방문 표시 잘 되는지 확인함

디버깅 : 18분
[1] 오픈테케 3번 답 이상하게 찍힘
* 아니나 다를까,, 인덱스 처리는 내가 제일 못하는 것,,,,
* 4번 구역이 2번 구역까지 포함해서 세고 있었음
* 중복 방문이라 방문배열 찍어보는 것만으로는 확인하지못했던 것
* 수정함

* 이 과정에서 디버거 돌리면서
* 엥 0번 열에서 시작하는 구획이 없네? 이상하다?
* 했는데 제출하고 보니까 결국 그것 때문에 틀렸습니다.

[2] d1의 범위 이슈
* 틀렸습니다 보자마자
* 아맞다,,, 제일 왼쪽에 도달 못했지
* 열이면 y쪽 , 0번 열이니까 d1관련 이슈겠거니 해서 그쪽으로 찾아감
* 아니나다를까 x, y 를 0부터 시작하면 부등식 자체가 바뀌어야함,,,,,,,,,,,,,,

[시간 복잡도]
* x, y, d1, d2 결정하는 경우의 수 대강 NC3*N
* 매 경우마다 전체를 다 보니까 N**2이 추가로 곱해짐
* 대강 N**6 이니까 넉넉친 않지만 가능

[엣지 케이스] : 다 같은경우 (차이0)
5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1


def compute(x, y, d1, d2):
    global ans

    visited = [[0]*N for _ in range(N)]
    # 각 구역의 인구 수
    people = [0]*5

    # 1번 구역 표시 및 인구 더하기
    for i in range(x+d1):
        coledge = y+1
        if i>=x: coledge = y-(i-x)
        for j in range(coledge):
            visited[i][j]=1
            people[0]+=arr[i][j]

    # 2번 구역 표시 및 인구 더하기
    for i in range(x+d2+1):
        coledge = y+1
        if i>=x: coledge = y+(i-x)+1
        for j in range(coledge, N):
            visited[i][j]=1
            people[1]+=arr[i][j]

    # 3번 구역 표시 및 인구 더하기
    for i in range(x+d1, N):
        coledge = y-d1+d2
        if i<=x+d2+d1: coledge = y-d1+d2 - (x+d2+d1-i)
        for j in range(coledge):
            visited[i][j]=1
            people[2]+= arr[i][j]

    # 4번 구역 표시 및 인구 더하기
    for i in range(x+d2+1, N):
        coledge = y-d1+d2
        if i<=x+d1+d2: coledge = y-d1+d2 +(x+d1+d2-i)+1
        for j in range(coledge, N):
            visited[i][j]=1
            people[3]+=arr[i][j]

    # 5번 구역 인구 더하기
    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            people[4]+=arr[i][j]

    ans = min(ans, max(people)-min(people))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 40000
# x, y, d1, d2 정하기
for x in range(N):
    for y in range(N):
        # 1<=y-d1은 y>=1 이기 때문에 있었던 조건이라서
        # y 범위를 0이상 N미만으로 잡은 나에게는
        # 0<=y-d1 으로 바꿔 생각해야했던 부분
        for d1 in range(1, y + 1):
            for d2 in range(1, N - y):
                if d2 > N - x - d1 - 1: continue
                compute(x, y, d1, d2)
print(ans)
'''