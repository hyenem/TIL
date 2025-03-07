N = int(input())
left = 1
right = N
while left<=right:
    mid = (left+right)//2
    if mid**2==N:       #mid의 제곱과 비교
        print(mid)
        break
    elif mid**2<N:
        left=mid+1
    else :
        right = mid-1