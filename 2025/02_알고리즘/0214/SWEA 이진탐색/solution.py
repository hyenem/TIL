T = int(input())
for tc in range(1, T+1):
    N, D = map(int, input().split())
    arr = list(map(int, input().split()))
    left = 0
    right = N-1
    ans = 0
    while left<=right:
        mid = (left+right)//2
        if arr[mid]==D:
            ans = mid+1
            break
        elif arr[mid]>D:
            right = mid-1
        else :
            left = mid+1
    print(f'#{tc} {ans}')