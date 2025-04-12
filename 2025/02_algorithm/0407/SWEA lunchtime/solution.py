from collections import deque

def calculate():
    global ans
    atime1 = sorted(s1, reverse=True)
    atime2 = sorted(s2, reverse=True)

    etime1, etime2=0, 0
    if atime1:
        if len(atime1)<=3:
            etime1 = atime1[0]+stair[0][2]
        else:
            q = deque()
            for _ in range(3):
                q.append(atime1.pop()+stair[0][2])

            while atime1:
                q.append(max(q.popleft(), atime1.pop())+stair[0][2])

            while q:
                etime1 = q.popleft()

    if atime2:
        if len(atime2) <= 3:
            etime2 = atime2[0] + stair[1][2]
        else:
            q = deque()
            for _ in range(3):
                q.append(atime2.pop() + stair[1][2])

            while atime2:
                q.append(max(q.popleft(), atime2.pop()) + stair[1][2])

            while q:
                etime2 = q.popleft()

    if ans==-1:
        ans = max(etime1, etime2)
    else:
        ans = min(ans, max(etime1, etime2))

def btk(idx):
    if idx==len(people):
        calculate()
        return

    s1.append(dist[idx][0])
    btk(idx+1)
    s1.pop()

    s2.append(dist[idx][1])
    btk(idx+1)
    s2.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stair = []
    people = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                people.append((i, j))
            elif arr[i][j]>=2:
                stair.append((i, j, arr[i][j]))

    dist = []
    for x, y in people:
        d1 = abs(x-stair[0][0])+abs(y-stair[0][1])
        d2 = abs(x-stair[1][0])+abs(y-stair[1][1])
        dist.append((d1, d2))

    s1 = []
    s2 = []
    ans = -1
    btk(0)
    print(f'#{tc} {ans+1}')