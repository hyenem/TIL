def solution(start, end):
    if start==end:
        return start
    mid = (start+end)//2
    first = solution(start, mid)
    second = solution(mid+1, end)
    if arr[first]==3:
        if arr[second]==1: return second
        return first
    else :
        if arr[second]==arr[first]+1:
            return second
        return first


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = solution(0, N-1)+1
    print(f'#{tc} {ans}')