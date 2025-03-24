def solution(i):        #i행에 대한 선ㄴ택
    global ans
    if i==N:
        ans += 1
        return
    for k in range(N):  #k열 선택
        if visited[k]: continue
        if visited_sum[i+k]:continue
        if visited_sub[i-k+N]:continue

        visited[k]=True
        visited_sum[i + k]=True
        visited_sub[i - k + N] = True
        solution(i+1)
        visited[k] = False
        visited_sum[i + k] = False
        visited_sub[i - k + N] = False

N = int(input())
visited = [False]*N
#대각선 방문확인
visited_sum = [False]*(2*N)
visited_sub = [False]*(2*N)

ans = 0
solution(0)
print(ans)