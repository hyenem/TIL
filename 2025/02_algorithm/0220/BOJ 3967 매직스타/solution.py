def solution(idx):
    global flag
    if flag: return
    if idx==len(choice):
        flag = True
        for i in range(len(choice)):
            arr[choice[i][0]][choice[i][1]]=chr(ans[i]-1+ord('A'))
        for ele in arr:
            print(''.join(ele))
        return True
    for i in range(1, 13):
        if visited[i]: continue
        l1, l2 = points[choice[idx]]
        summ[l1]+=i
        summ[l2]+=i
        if summ[l1]>26 or summ[l2]>26:
            summ[l1] -= i
            summ[l2] -= i
            return
        visited[i]=True
        ans.append(i)
        solution(idx+1)
        ans.pop()
        summ[l1]-=i
        summ[l2]-=i
        visited[i]=False

arr = [list(input()) for _ in range(5)]
visited = [False]*13
summ = [0]*6
points={(0,4):(0,2), (1,3):(0,1), (2,2):(0,4), (3,1):(0,5), (1,1):(1,4), (1,5):(1,2), (1,7):(1,3), (2,6):(2,3), (3,7):(2,5), (3,5):(3,5), (4,4):(3,4), (3,3):(4,5)}
choice = []
ans = []
flag = False
for i in range(5):
    for j in range(9):
        if arr[i][j]=='x':
            choice.append((i,j))
        elif arr[i][j]=='.':continue
        else :
            for k in points[(i,j)]:
                summ[k]+=ord(arr[i][j])-ord('A')+1
                visited[ord(arr[i][j])-ord('A')+1]=True
solution(0)