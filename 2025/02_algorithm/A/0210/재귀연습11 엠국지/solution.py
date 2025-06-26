def solution(idx, summ, num):
    global cnt
    if num>M:
        return
    if num==M and summ==K:
        cnt+=1
        return
    for i in range(idx+1, N):
        solution(i, summ+arr[i], num+1)

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    solution(-1, 0, 0)
    print(f'#{tc} {cnt}')


def solution(n, arr):
    if n==5:
        print(arr)
        return
    solution(n+1, arr+[1])
    solution(n+1, arr+[2])

solution(0,[])