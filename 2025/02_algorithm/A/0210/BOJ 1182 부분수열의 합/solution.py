def solution(idx, summ, cnt):
    global ans
    if cnt>0 and summ==S:
        ans+=1
    for i in range(idx+1, N):
        solution(i, summ+arr[i], cnt+1)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
solution(-1, 0, 0)
print(ans)