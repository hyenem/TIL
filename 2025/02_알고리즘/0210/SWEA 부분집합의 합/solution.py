def solution(idx, cnt, summ):
    global ans
    if cnt>N or summ>K:
        return
    if cnt==N and summ==K:
        ans+=1
        return
    for i in range(idx+1, 13):
        solution(i, cnt+1, summ+i)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    ans = 0
    solution(0, 0, 0)
    print(f'#{tc} {ans}')