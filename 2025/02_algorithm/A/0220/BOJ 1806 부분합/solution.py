N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = N+1
left = -1
right = 0
summ = arr[0]
while left<right:
    if summ>=S:
        ans = min(right-left, ans)
        left+=1
        summ-=arr[left]
    else :
        right+=1
        if right==N: break
        summ+=arr[right]
if ans == N+1:
    print(0)
else:
    print(ans)
