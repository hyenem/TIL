def solution(visited, arr):
    if len(arr)==N:
        print(*arr)
        return
    for i in range(1, N+1):
        if visited&(1<<i)==0:
            solution(visited|(1<<i), arr+[i])

N = int(input())
solution(0,[])