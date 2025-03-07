def binary(left, right):
    while left<=right:
        mid = (left+right)//2
        cnt = 0
        before = 0
        idx = 1
        while idx<n+1:
            if arr[idx]-arr[before]>=mid:
                cnt+=1
                before = idx
            idx+=1
        if cnt < n-m:
            right = mid-1
        else :
            left = mid + 1
    print(right)

d, n, m = map(int,input().split())
arr = [0]+[int(input()) for _ in range(n)]
arr.sort()
binary(0, d-arr[-1])