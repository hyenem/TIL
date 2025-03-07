def solution(idx, cnt):
    global ans
    if idx>=2*N-2:
        return cnt
    x, y= start_idx[idx]
    print(visited_sub)
    tmp=0
    # tmp=solution(idx+2, cnt)
    for i in range(cnt_idx[idx]):
        if arr[x-i][y+i]==0:continue
        if visited_sub[x-y-i-i+N]: continue
        visited_sub[x-y-i-i+N]=True
        tmp=max(solution(idx+2, cnt+1), tmp)
        visited_sub[x-y-i-i+N]=False
    return tmp


N = int(input())
if N==1:
    print(input())
else :
    start_idx =[(i,0) for i in range(N)]+[(N-1,i) for i in range(1, N-1)]
    cnt_idx =[i for i in range(1, N+1)]+[N-i for i in range(1, N)]
    print(start_idx)
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited_sub = [False]*(2*N)
    ans = solution(0,0)+solution(1,0)
    print(ans)
