N = int(input())
arr = [0]+list(map(int, input().split()))
idx = [0]*(N+1)
for i in range(1, N+1):
    idx[arr[i]]=i

visited = [False]*(N+1)
tmp = []
for i in range(1, N+1):
    if arr[i]==i or visited[i]:
        continue
    com = [arr[i]]
    visited[arr[i]]=True
    while com[-1]!=i:
        visited[arr[com[-1]]]=True
        com.append(arr[com[-1]])
    tmp.append(com)
if len(tmp)==0:
    print(0)
elif len(tmp)==1:
    print(1)
    print(f'{len(tmp[0])}:', *tmp[0])
else :
    tmp = list(zip(*tmp))
    ttmp = arr[tmp[0][-1]]
    for i in range(len(tmp[0])-1, 0, -1):
        arr[tmp[0][i]]=arr[tmp[0][i-1]]
    arr[tmp[0][0]]=ttmp
    ans =[tmp[0]]
    com = [arr[tmp[1][0]]]
    while len(com)==1 or com[-1] != com[0]:
        com.append(arr[com[-1]])
    ans.append(com)
    com.pop()

    print(len(ans))
    for com in ans:
        if len(com)!=0: print(f'{len(com)}:', *com)