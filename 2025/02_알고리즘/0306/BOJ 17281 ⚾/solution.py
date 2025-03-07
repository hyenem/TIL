from collections import deque
import sys
input = sys.stdin.readline

# 계산
def compute():
    global ans
    score = 0
    q = deque(order)
    loc = []
    for i in range(N):
        if score + acc[i] <=ans: return

        row = arr[i]
        loc.clear()

        # 아웃 3개 될때까지
        out = 0
        while out<3:
            player = q.popleft()
            q.append(player)

            if row[player]==0:
                out += 1
            else :
                score+=1
                loc.append(row[player])

        if len(loc)==0: continue
        # 쌓아놓은 타자들 중
        # 골인 못한 타자 제외하기
        idx = len(loc)-1
        cnt = 0
        while idx>=0 and cnt+loc[idx]<4:
            score -= 1
            cnt += loc[idx]
            idx -= 1
    ans = max(ans, score)

# 조합
def permutation(j):
    if ans == acc[0] : return

    if j==9:
        compute()
        return

    if j==3:
        permutation(j+1)
        return

    for i in range(1, 9):
        if visited[i]: continue
        visited[i]=1
        order[j]=i
        permutation(j+1)
        visited[i]=0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
summ = [0]*N

# 가지치기를 위한 누적배열
for i in range(N):
    zerocnt = 0
    for j in range(9):
        if arr[i][j]!=0:
            summ[i]+=1
        else :
            zerocnt+=1
    # 해당 행의 최대 획득 점수
    summ[i]*=4-min(zerocnt, 3)
# 최대 획득 점수 누적
acc = summ[:]
for i in range(N-2, -1, -1):
    acc[i] += acc[i+1]

order = [0]*9
visited = [0]*9
visited[0]=1

ans = 0
permutation(0)

print(ans)