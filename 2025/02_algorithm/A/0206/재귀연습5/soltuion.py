def solution(N):
    if N==1 or N==2:
        return 1
    return solution(N-1)+solution(N-2)

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc} {solution(int(input()))}')