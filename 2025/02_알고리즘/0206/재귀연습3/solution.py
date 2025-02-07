# 지금까지의 누적합, 이번에 더해줄 수
def solution(acc, cnt):
    if cnt==0:
        print(acc)
        return
    solution(acc+cnt, cnt-1)

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    solution(0, int(input()))