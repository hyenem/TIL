N = int(input())
arr = list(map(int, input().split()))
M = int(input())
left = 0
right = max(arr)
ans = 0
if sum(arr)<M:
    ans = right
else :
    while left<=right:
        mid = (left+right)//2
        amount = 0
        for ele in arr:
            amount+=min(ele, mid)
        if amount==M:
            ans = mid
            break
        elif amount < M:
            ans = max(ans, mid)
            left = mid+1
        else :
            right = mid-1
print(ans)