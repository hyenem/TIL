N = int(input())
arr = list(map(int, input().split()))

left = 0
right = N-1
summ = arr[-1]+arr[0]
ans = [abs(summ), arr[0], arr[-1]]
while left<right:
    if summ<0:
        summ-=arr[left]
        left+=1
        if left==right: break
        summ+=arr[left]
        if abs(summ)<ans[0]:
            ans[0]=abs(summ)
            ans[1]=arr[left]
            ans[2]=arr[right]
    elif summ>0 :
        summ-=arr[right]
        right-=1
        if right==left: break
        summ+=arr[right]
        if abs(summ)<ans[0]:
            ans[0]=abs(summ)
            ans[1]=arr[left]
            ans[2]=arr[right]
    else :
        break
print(ans[1], ans[2])
