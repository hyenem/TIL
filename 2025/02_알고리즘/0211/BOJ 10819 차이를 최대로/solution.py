def solution(cnt, beforeidx, visited, summ):
    global ans
    if cnt==N:
        ans = max(ans, summ)
        return
    for i in range(N):
        if visited&(1<<i)!=0: continue
        # 처음으로 골라지는 숫자는 그냥 저장만하기
        if cnt == 0:
            solution(cnt+1, i, visited|(1<<i), summ)
        # 두번째부터 골라지는 숫자는
        # 이전 숫자와의 차이를 계산해서 합에 누적해주기
        else :
            solution(cnt+1, i, visited|(1<<i), summ+abs(arr[beforeidx]-arr[i]))


N = int(input())
arr = list(map(int, input().split()))
ans = 0
solution(0, -1, 0, 0)
print(ans)
