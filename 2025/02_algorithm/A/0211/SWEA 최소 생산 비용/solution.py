def solution(idx, visited, summ):
    global ans
    # 이미 저장되어있는 최솟값보다 커지면 계산할 필요 없음
    if summ>=ans:
        return
    if idx==N:
        ans = min(summ, ans)
        return
    # idx행의 j열 선택하기
    for i in range(N):
        if (visited>>i)&1==1:
            continue
        solution(idx+1, visited|(1<<i), summ+arr[idx][i])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans =100*N
    solution(0, 0, 0)
    print(f'#{tc} {ans}')
