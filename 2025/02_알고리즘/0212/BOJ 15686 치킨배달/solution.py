def solution(idx, arr, cnt):
    global ans
    # m개 다 뽑으면
    if cnt==M:
        summ = 0
        for ele in arr:
            summ+=ele
        ans = min(ans, summ)
        return
    for i in range(idx+1, len(chicken)):
        nextarr = arr[:]
        # i 번째 치킨집을 선택했을때
        # 각 집의 치킨거리 계산
        for j in range(len(house)):
            nextarr[j]=min(arr[j], abs(chicken[i][0]-house[j][0])+abs(chicken[i][1]-house[j][1]))
        solution(i, nextarr, cnt+1)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []

for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            house.append((i,j))
        elif arr[i][j]==2:
            chicken.append((i, j))

dis = [100]*len(house)
ans = 100*len(house)
solution(-1, dis,  0)
print(ans)