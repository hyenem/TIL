def quick(start, end):
    if start>=end: return
    pivot = start
    left = pivot+1
    right = end
    while left<=right:
        while left<=right and arr[left]<=arr[pivot]:
            left+=1
        while left<=right and arr[right]>=arr[pivot]:
            right -=1
        if left<right:
            tmp = arr[left]
            arr[left]=arr[right]
            arr[right]=tmp
    tmp = arr[pivot]
    arr[pivot]=arr[right]
    arr[right]=tmp
    quick(start, right - 1)
    quick(right + 1, end)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick(0, N - 1)
    print(f'#{tc} {arr[N//2]}')