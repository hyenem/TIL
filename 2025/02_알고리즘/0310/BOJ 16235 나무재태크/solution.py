'''
제출횟수 : 1회
풀이시간 : 45분

! 명심할 것 !
* 문제 내 멋대로 넘겨짚지 말것
>> 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
[오해한 부분] 나무가 양분 1개 먹고 1 증가한다고 생각함

구상 : 5분
* tree라는 배열의 i, j에 해당 칸의 모든 나무들의 나이를 집어넣기로함
* 어린 나무를 어떻게 추가할지 생각함
* 우선 insert(0, 1)로 처리해서 sort를 안하도록 해봄

구현 : 18분
* 원래는 tree_exist 라는 set으로 N^2 다 안돌고 처리하려했는ㄷ
* remove해주는 시간도 무시하지 못할 것 같아서 그냥 전체 순회하기로함

디버깅 : 22분
* 나무가 자기 나이만큼 양분을 먹어야한다는걸 캐치하는데 7분 소요
* 대공사 진행함

[리팩토링]
[1]
insert(0, 1)을 하는게 영 찝찝해서
맨 뒤에 추가하고 뒤에서부터 처리하는 것으로 바꿈
그 과정에서 stack을 사용하면 코드가 깔끔해질 것 같아서
springsummer에서 stack을 사용함


[2]
준영프로님 코드 보고 리팩토링함
나이가 같은 나무들이 있으면 한꺼번에 처리


[시간 복잡도]
(리팩토링 전)
대강 K*(N^2*8*K) 의 상수배
8*10**8 이라 찝찝,,, 아레 엣지케이스를 통과하지 못함
(리팩토링 후)
K*(N^2*100) -> 나무가 100살보다 더 먹을순 없음
아래 엣지케이스 통과 가능


[엣지 케이스] : 가장 오래걸리는경우
                일단 내건 통과 못할듯
10 100 1000
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
0 0 4
0 1 4
0 2 4
0 3 4
0 4 4
0 5 4
0 6 4
0 7 4
0 8 4
0 9 4
1 0 4
1 1 4
1 2 4
1 3 4
1 4 4
1 5 4
1 6 4
1 7 4
1 8 4
1 9 4
2 0 4
2 1 4
2 2 4
2 3 4
2 4 4
2 5 4
2 6 4
2 7 4
2 8 4
2 9 4
3 0 4
3 1 4
3 2 4
3 3 4
3 4 4
3 5 4
3 6 4
3 7 4
3 8 4
3 9 4
4 0 4
4 1 4
4 2 4
4 3 4
4 4 4
4 5 4
4 6 4
4 7 4
4 8 4
4 9 4
5 0 4
5 1 4
5 2 4
5 3 4
5 4 4
5 5 4
5 6 4
5 7 4
5 8 4
5 9 4
6 0 4
6 1 4
6 2 4
6 3 4
6 4 4
6 5 4
6 6 4
6 7 4
6 8 4
6 9 4
7 0 4
7 1 4
7 2 4
7 3 4
7 4 4
7 5 4
7 6 4
7 7 4
7 8 4
7 9 4
8 0 4
8 1 4
8 2 4
8 3 4
8 4 4
8 5 4
8 6 4
8 7 4
8 8 4
8 9 4
9 0 4
9 1 4
9 2 4
9 3 4
9 4 4
9 5 4
9 6 4
9 7 4
9 8 4
9 9 4
'''

def springsummer():
    # 어린 나무일수록 뒤에 있음
    for x in range(N):
        for y in range(N):
            stack = []
            # 뒤에서부터 보면서 양분을 흡수할 수 있으면 흡수하고
            # 살아있는 나무를 stack 배열에 저장
            while tree[x][y] and energy[x][y] - tree[x][y][-1][0] >= 0:
                num = min(tree[x][y][-1][1], energy[x][y]//tree[x][y][-1][0])
                energy[x][y] -= tree[x][y][-1][0]*num
                if num==tree[x][y][-1][1]:
                    grow = tree[x][y].pop()
                    grow[0]+=1
                    stack.append([grow[0], grow[1]])
                else :
                    tree[x][y][-1][1] -= num
                    stack.append([tree[x][y][-1][0]+1, num])

            # 위의 while 문을 거치고 남은 나무는 죽은 나무
            # 죽은 나무는 땅의 양분이 되어주기
            while tree[x][y]:
                dead = tree[x][y].pop()
                energy[x][y] += (dead[0] // 2)*dead[1]

            # stack에 있는 것 다시 나무에 넣기
            # 이렇게 해야만 순서가 유지됨
            while stack:
                tree[x][y].append(stack.pop())


def fall():
    for x in range(N):
        for y in range(N):
            for z, num in tree[x][y]:
                # 5의 배수이면 주변에 나무 추가하기
                # 이 시점에 바로 추가해도 되는 이유는
                # 무조건 나이가 1인 나무만 추가되기때문
                if z % 5 == 0:
                    for dx, dy in ((0, 1), (0, -1), (1, 1), (1, -1), (1, 0), (-1, 1), (-1, -1), (-1, 0)):
                        nx, ny = x + dx, y + dy
                        if not (0 <= nx < N and 0 <= ny < N): continue
                        if tree[nx][ny] and tree[nx][ny][-1][0]==1:
                            tree[nx][ny][-1][1]+=num
                        else :
                            tree[nx][ny].append([1, num])
                elif z < 5:
                    break


def winter():
    for i in range(N):
        for j in range(N):
            energy[i][j] += A[i][j]


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
start = [list(map(int, input().split())) for _ in range(M)]
energy = [[5] * N for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]

# 각 칸의 나무의 나이를 저장
for x, y, z in start:
    tree[x - 1][y - 1].append([z, 1])

for _ in range(K):
    springsummer()
    fall()
    winter()

ans = 0
for i in range(N):
    for j in range(N):
        ans += sum(map(lambda x: x[1], tree[i][j]))

print(ans)