def solution(idx, summ):
    global ans
    if summ>ans: return
    # 장훈이 키보다 커지면 정답갱신
    if summ>=B:
        ans = min(ans, summ)
        return
    # i번째 사람을 포함하면 누적키
    for i in range(idx+1, N):
        solution(i, summ+arr[i])

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    ans = 10000*N
    arr= list(map(int, input().split()))
    solution(-1, 0)
    print(f'#{tc} {ans-B}')