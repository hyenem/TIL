import sys
input = sys.stdin.readline

def pang():
    global ans

    tmpans = N
    nstack = []
    for color, cnt in stack:
        if cnt==0: continue
        if nstack and nstack[-1][0] == color:
            nstack[-1][1] += cnt
        elif nstack and nstack[-1][1]>=4:
            tmpans -= nstack.pop()[1]
            if nstack and nstack[-1][0]== color:
                nstack[-1][1]+=cnt
            else :
                nstack.append([color, cnt])
        else:
            nstack.append([color, cnt])

    if nstack and nstack[-1][1]>=4:
        tmpans-=nstack.pop()[1]

    ans = min(ans, tmpans)

N = int(input())
lst = [int(input()) for _ in range(N)]
stack = []
for c in lst:
    if stack and stack[-1][0] == c:
        stack[-1][1] += 1
    else:
        stack.append([c, 1])

ans = N
for i in range(len(stack)):
    if i!=0:
        if stack[i-1][1]==1 and (i==1 or (stack[i-2][0]!=stack[i][0] and (i==len(stack)-1 or stack[i-2][0]!=stack[i+1][0]))):
            ans = min(ans, N-stack[i][1]-1)
        elif stack[i-1][1]!=1 and (i==len(stack)-1 or (stack[i+1][0]!=stack[i-1][0])):
            ans = min(ans, N-stack[i][1]-1)
        else :
            tmp = stack[i-1][:]
            stack[i - 1][1] -= 1
            stack[i][1] += 1
            pang()
            stack[i - 1][1] += 1
            stack[i][1] -= 1

    if i!=len(stack)-1:
        if stack[i+1][1]==1 and (i==len(stack)-2 or (stack[i+2][0]!=stack[i][0] and (i==0 or stack[i+2][0]!=stack[i-1][0]))):
            ans = min(ans, N-stack[i][1]-1)
        elif stack[i+1][1]!=1 and (i==0 or stack[i-1][0]!=stack[i+1][0]):
            ans = min(ans, N-stack[i][1]-1)
        else :
            stack[i+1][1] -= 1
            stack[i][1] += 1
            pang()
            stack[i + 1][1] += 1
            stack[i][1] -= 1

print(ans)