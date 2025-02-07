def solution(N, T):
    print(N, end=' ')
    if N<T:
        solution(N+1, T)

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    solution(0, int(input()))
    print()