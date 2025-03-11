'''
갓준영!
-> 나무를 어떤 나이에 몇개있는지 처리

[시간 복잡도]
K*(N^2*100) -> 나무가 100살보다 더 먹을순 없음
아래 엣지케이스 통과 가능
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