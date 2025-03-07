def solution(idx, cnt, accR, accG, accB):
    global d
    if cnt>=2:
        newR, newG, newB = accR//cnt, accG//cnt, accB//cnt
        d=min(d, abs(newR -R)+ abs(newG-G)+abs(newB-B))
    if cnt==7: return
    for i in range(idx+1, N):
        solution(i, cnt+1, accR+arr[i][0], accG+arr[i][1], accB+arr[i][2])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
R, G, B = map(int, input().split())

d = 255*3+1
solution(-1, 0, 0, 0, 0)
print(d)