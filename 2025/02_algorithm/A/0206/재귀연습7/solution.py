def solution(N):
    if N%10==0:
        return N
    return solution(N//10)+N%10

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc} {solution(int(input()))}')
