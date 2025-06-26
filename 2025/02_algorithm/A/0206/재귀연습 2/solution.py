def solution(N):
    print(N, end=' ')
    if N>1:
        solution(N-1)

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    solution(int(input()))
    print()