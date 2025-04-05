def dist(sx, sy, ex, ey):
    return abs(sx-ex)+abs(sy-ey)

def solution(x, y, h, d, acc):
    global ans
    if dist(x, y, ex, ey)<=h+d:
        if ans ==-1: ans = acc+dist(x, y, ex, ey)
        else : ans = min(ans, acc+dist(x, y, ex, ey))
        return

    for i in range(len(umb)):
        if used[i]: continue
        ux, uy = umb[i]
        if dist(x, y, ux, uy)<=h+d:
            if h-max(0, (dist(x, y, ux, uy)-d))>=0:
                used[i]=1
                solution(ux, uy, h-max(0, (dist(x, y, ux, uy)-d)), D, acc+dist(x, y, ux, uy))
                used[i]=0


N, H, D = map(int, input().split())
arr = [list(input()) for _ in range(N)]
umb = []
for i in range(N):
    for j in range(N):
        if arr[i][j]=='S':
            x, y = i, j
        elif arr[i][j]=='U':
            umb.append((i, j))
        elif arr[i][j]=='E':
            ex, ey = i, j

used = [0]*len(umb)
ans = -1
solution(x, y, H, 0, 0)
print(ans)