N, M = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
right = max(arr)
ans = 0
while left<=right:
    mid = (left+right)//2
    amount = 0
    for ele in arr:                #가져갈수있는 나무 양 계산
        amount += max(0, ele-mid)
    if amount==M:
        ans = mid
        break
    elif amount<M:                # 작으면 높이 낮추기
        right = mid-1
    else :                        # 크면 높이 높히기
        ans = max(ans, mid)
        left = mid+1
print(ans)