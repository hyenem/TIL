'''2회독
제출횟수 : 1회
풀이시간 : 8분

* 쉬운 문제라 피드백 할 것 없음
'''

def btk(idx):
    global ans, dist
    if len(selected)==M:
        ans = min(ans, sum(dist))
        return

    for i in range(idx, len(hospital)):
        tmp = dist[:]
        hx, hy = hospital[i]
        selected.append(i)
        for p in range(len(people)):
            px, py = people[p]
            dist[p]=min(dist[p], abs(px-hx)+abs(py-hy))
        btk(i+1)
        selected.pop()
        dist = tmp


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
hospital = []
people = []
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            people.append((i, j))
        elif arr[i][j]==2:
            hospital.append((i, j))

selected = []
dist = [2*N+1]*len(people)
ans = (2*N+1)*len(people)
btk(0)
print(ans)

'''1회독
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
'''