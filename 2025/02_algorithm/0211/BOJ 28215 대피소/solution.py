# 이전 선택된 집의 인덱스
# 지금까지 처리된 집의 수
# 지금까지 골라진 대피소들과 각 집까지 거리의 최솟값
def solution(idx, cnt, arr):
    global ans
    # K개의 집을 다 골랐으면
    # 거리중 최댓값을 정답에 갱신
    if cnt == K:
        ans = min(ans, max(arr))
        return
    for i in range(idx+1, N):
        # 넘겨온 arr를 복사해서(슬라이싱으로 깊은복사)
        # i번째 집이 대피소가 되므로서 최소가 되는 거리를 계산, 갱신
        thisarr = arr[:]
        for j in range(N):
            thisarr[j] = min(thisarr[j], abs(house[i][0]-house[j][0])+abs(house[i][1]-house[j][1]))
        solution(i, cnt+1, thisarr)


N, K = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(N)]
# 최대 거리는 10000*2
ans = 200000
solution(-1, 0, [200000]*N)
print(ans)