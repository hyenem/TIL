def solution(sum):
    if M-(N-len(ans))*6>sum or sum>M:
        return
    if sum==M and len(ans)==N:
        print(*ans)
    for i in range(1, 7):
        ans.append(i)
        solution(sum+i)
        ans.pop()

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = []
    print(f'#{tc}')
    solution(0)
