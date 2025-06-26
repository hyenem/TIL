message = input()
N = int(input())
arr = [0]
# N명의 사람에 대해 범인이다 / 아니다 라고 말한 사람
tf = [[0]*(N+1) for _ in range(2)]
# 1을 진술한 사람 수
cnt = 0
for i in range(N):
    M = int(input())
    S = list(map(int, input().split()))
    B = int(input())
    arr.append((B, S))
    if B==1:
        cnt+=1
    for ele in S:
        tf[B][ele] += 1

ans = []
for i in range(1, N+1):
    B, S = arr[i]
    if B==1 and i in S: continue
    elif B==0 and i not in S : continue

    if B==0 and i in S: tf[0][i]-=1
    elif B==1 and i in S: tf[1][i]-=1

    if tf[0][i]>=1: continue
    if cnt - B - tf[1][i]>0:
        continue

    ans.append(i)

    if B==0 and i in S: tf[0][i]+=1
    elif B==1 and i in S: tf[1][i]+=1

if len(ans)==0:
    print('swi')
else:
    print(*ans)
