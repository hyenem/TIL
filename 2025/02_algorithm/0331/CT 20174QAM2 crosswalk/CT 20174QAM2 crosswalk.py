'''2회독
제출횟수 : 1회
풀이시간 : 15분

* 인덱스로 접근하는 것 들이 약하고,, 두려움도 있음,,,
* 디테일한 인덱스 처리를 해야하는 경우 구체적인 예시를 직접 해볼것

'''

def check(lst):
    visited = [0]*N
    for i in range(N-1):
        if lst[i]==lst[i+1]: continue
        if abs(lst[i]-lst[i+1])!=1:
            return 0

        if lst[i]-1==lst[i+1]:
            if i>=N-L:
                return 0
            for j in range(i+1, i+L+1):
                if lst[j]!=lst[i+1]:
                    return 0
                if visited[j]: return 0

                visited[j]=1

    lst = lst[::-1]
    visited = visited[::-1]

    for i in range(N - 1):
        if lst[i] == lst[i + 1]: continue
        if abs(lst[i] - lst[i + 1]) != 1:
            return 0

        if lst[i] - 1 == lst[i + 1]:
            if i >= N - L:
                return 0
            for j in range(i + 1, i + L+1):
                if lst[j] != lst[i + 1]:
                    return 0
                if visited[j]: return 0

                visited[j] = 1
    return 1

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    ans += check(arr[i])

arr = list(map(list, zip(*arr)))
for i in range(N):
    ans += check(arr[i])

print(ans)