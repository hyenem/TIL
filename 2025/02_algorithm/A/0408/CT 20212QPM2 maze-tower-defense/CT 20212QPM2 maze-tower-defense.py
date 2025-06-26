'''2회독
제출횟수 :4회
* stack에서 첫번쨰 원소처리 안함
* 터지고 합칠 때 마지막 원소 안보게 인덱스 설정 되어있음
* N*N넘치는 애들 처리 안함
풀이시간 : 40분

* N회독이라고 문제를 설읽지말라고~!!!!!!!!!!!!!!!!!!!!!!!!
'''

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cmds = [list(map(int, input().split())) for _ in range(M)]
dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0))

popidx = []
for d in range(4):
    lst = [((2-d)%4)*2+1]
    acc = lst[-1]
    for _ in range(N//2-1):
        acc += 8
        lst.append(lst[-1]+acc)
    popidx.append(lst)

lst = [0]
x, y = N//2, N//2
r = 1
d = 3
ans = 0
while True:
    r+=1
    d=(d-1)%4
    dx, dy = dxdy[d]
    for _ in range(r//2):
        x, y = x+dx, y+dy
        if arr[x][y]==0: break
        lst.append(arr[x][y])
        if (x, y)==(0,0): break
    else:
        continue
    break

for d, p in cmds:
    for i in range(p-1, -1, -1):
        idx = popidx[d][i]
        if idx>=len(lst): continue
        ans += lst[idx]
        del lst[idx]

    stack = []
    for k in lst:
        if stack and stack[-1][1]==k:
            stack[-1][0]+=1
        else:
            stack.append([1, k])

    end = 0
    while not end:
        end = 1

        for i in range(len(stack)-1, -1, -1):
            if stack[i][0]>=4:
                end = 0
                ans += stack[i][0]*stack[i][1]
                del stack[i]

        for i in range(len(stack)-1, 0, -1):
            if stack[i][1]==stack[i-1][1]:
                stack[i-1][0]+=stack[i][0]
                del stack[i]

    lst = [0]
    stack.pop(0)
    stack = stack[:(N*N-1)//2]
    for ele in stack:
        lst.extend(ele)

print(ans)

'''
제출횟수 : 2회
    * 틀렸습니다 1회
            for i in range(1, min(len(stack), (N*N-1)//2)):   # 칸에 넘치기 전까지 변환해서 구슬 넣기
                    lst+=stack[i]
        이렇게 하면 N^2 개 될거라고 생각했는데,,, 1에서 시작하더라 ?!?!??! ㅠㅜ
        머리 오만삼천팔백대 딱콩하기
풀이시간 : 79분

[ 고전한 이유 ]
* 구슬이 4개 이상이면 터트리는거자나아아아아아앙아아아렁라ㅓ나ㅓㅁㄴㅇㄹ;ㅏㅁㅇ루ㅏㄴㅇㄹ;ㅜㅏ;ㅇ닐
  3개 이상이 아니자나ㅣㅇ나멀다ㅣ애;ㅡ;ㄹㄴ우ㅏ;ㅜㅏㅏㅜ리ㅏㅜㅜㅏㅜㅏㅣㅁㅇ루ㅏㅣ루ㅏㅣㅇ니ㅓ;마;ㅇ러ㅏ
* 터트리기도 누적해두고 하려다가 그럴 이유가 없다는 걸 깨닳음,,,,, 그거 수정하는데 시간 들었음

[ 시간 복잡도 ]
M*N^3 보다는 작다
100*125000

[ 엣지 케이스 ] : 텅 빈 칸에도 얼음 결정이 떨어지는 경우
7 2
0 0 0 0 0 0 0
3 2 1 3 2 3 0
2 1 2 1 2 1 0
2 1 1 0 2 1 1
3 3 2 3 2 1 2
3 3 3 1 3 3 2
2 3 2 2 3 2 3
2 2
1 3

구상 : 10분
* 얼음 결정 떨어지는 칸의 규칙성 파악함
* 아예 누적 개수, 구슬 색인 리스트만 들고다니면 되겠다

구현 : 48분
* 구현 시작하고 26분까지 누적 개수 리스트로만 만들려고 하다가
    어차피 A, B 변환할 떄 누적 아닌 리스트가 생길 수 밖에 없다는 걸 깨닫고
    no누적리스트, 누적리스트의 교차로 가기로 함

디버깅 : 21분
[1] openTC 답이 안나와서 다 찍어봄
    -> 예시랑 진행상황이 달라서 보니깐,,,, 아니 4개부터 터트리는거임,,,
    -> 멍청하게 3개부터 터트린다,,,고짰다,,,,
    -> 제출 : 틀렸습니다. (75%)
[2] 다시 보니까 바~로 틀린이유 발견~~~~~ 1부터 (N^2-1)//2 까지 넣어서
    맵을 꽉채우게 넣을수가 없지롱~ 바보 혜민~~~



# 처음 이차원 배열을 일차원(달팽이 방향)으로 변환
def makelst():
    x, y, d = N // 2, N // 2-1, 0
    lst.append(arr[x][y])
    l = 2
    while (x != 0 or y != 0) and arr[x][y]!=0:
        l += 1
        d = (d + 1) % 4
        dx, dy = dxdy[d]
        for _ in range(l // 2):
            x, y = x + dx, y + dy
            if arr[x][y]==0: break
            lst.append(arr[x][y])
            if x == 0 and y == 0: break

# 연속되는 것 터트리고, 개수, 번호를 이용해서 변환하는 것 까지
def pop():
    global ans, lst

    # 몇개의 어떤구슬
    # 리스트를 쭉 돌면서 내 앞 구슬이랑 같으면 개수 하나 올리고
    # 아니면 1개의 lst[i] 색의 구슬이라고 추가해주기
    stack = [[0, 0]]
    for i in range(1, len(lst)):
        if lst[i]==stack[-1][1]:
            stack[-1][0]+=1
        else :
            stack.append([1, lst[i]])

    while True:                 # 해당 칸 없애기
        if end: break
        # 하나도 안터지면 그냥 끝내주려한다
        end = 1
        for i in range(len(stack)-1, 0, -1):
            if stack[i][0]>=4:                  # 4개이상인 것 터트리기
                end = 0
                ans += stack[i][0]*stack[i][1]  # 정답 추가하고
                del stack[i]

        for i in range(len(stack)-1, 0, -1):    # 뒤에서부터 쭉 돌면서 구슬 같으면
            if stack[i][1]==stack[i-1][1]:      # 날 지우고 내 앞에 구슬 수 더해줌
                stack[i-1][0]+=stack[i][0]
                del stack[i]

    lst = [0]
    ######################## 1부터 시작했으면,, 하나 더 더해줘야 그 개수지,,, #############
    for i in range(1, min(len(stack), (N*N-1)//2+1)):   # 칸에 넘치기 전까지 변환해서 구슬 넣기
        lst+=stack[i]


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = [0]
dxdy = ((0, -1), (1, 0), (0, 1), (-1, 0))

# 2차원 배열을 달팽이 모양으로 1차원으로 만들기
makelst()

magic = [tuple(map(int, input().split())) for _ in range(M)]
# 각 방향별 터지는 인덱스 처리
# 시작 인덱스를 기준으로 차이가 8씩 커지는 계차수열
dic = {1: [7], 2: [3], 3: [1], 4: [5]}
for i in range(1, 5):
    idx = dic[i]
    acc = idx[-1] + 8
    while idx[-1]+acc<N*N:
        idx.append(idx[-1]+acc)
        acc += 8

ans = 0
for d, s in magic:

    # 얼음 파편 떨어트리기
    poplst = dic[d]
    for i in range(s-1, -1, -1):
        idx = poplst[i]
        if len(lst)<=idx: continue
        del lst[idx]

    pop()

print(ans)
'''