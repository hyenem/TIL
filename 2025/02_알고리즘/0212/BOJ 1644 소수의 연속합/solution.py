N = int(input())
checkprime = [False]*2+[True]*(N-1)
prime = []
for i in range(2, N+1):
    if checkprime[i]:
        prime.append(i)
        for k in range(N//i+1):
            checkprime[k*i]=False

left = -1
right = -1
summ=0
ans = 0
M = len(prime)
while True:
    if summ == N:
        ans += 1
        right += 1
        if right==M: break
        summ+=prime[right]
    elif summ<N:
        right += 1
        if right == M: break
        summ += prime[right]
    else :
        left += 1
        summ -= prime[left]
print(ans)