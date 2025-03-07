def solution(n):
    if len(ans)==N:
        print(*ans)
        return
    for i in range(n, 7):
        ans.append(i)
        solution(i)
        ans.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = []
    print(f'#{tc}')
    solution(1)