def merge(start, end):
    global cnt
    mid = (start+end)//2
    if end-start<=1:
        return
    merge(start, mid)
    merge(mid, end)
    if arr[mid-1]>arr[end-1]: cnt+=1
    left, right = start, mid
    idx = start
    while left<mid and right<end:
        if arr[left]<arr[right]:
            newarr[idx]=arr[left]
            left+=1
        else :
            newarr[idx]=arr[right]
            right+=1
        idx+=1
    if left<mid:
        while left<mid:
            newarr[idx] = arr[left]
            left += 1
            idx+=1
    while right<end:
        newarr[idx] = arr[right]
        right+=1
        idx+=1
    for i in range(start, end):
        arr[i]=newarr[i]

T=int(input())
for tc in range(1, T+1):
    cnt = 0
    N = int(input())
    arr = list(map(int, input().split()))
    newarr=[0]*N
    merge(0, N)
    print(f'#{tc} {arr[N//2]} {cnt}')