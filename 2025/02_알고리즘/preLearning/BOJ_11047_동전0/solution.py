N, K = map(int, input().split())

coins = []
for _ in range(N):
    coin = int(input())
    if coin <= K:
        coins.append(coin)
coins.sort(reverse=True)
ans = K

def countcoin(startidx, acc, cnt):
    global ans
    if startidx==len(coins)-1 or acc+coins[startidx] > K:
        ans = min(ans, K-acc+cnt)
        return
    for i in range((K-acc)//coins[startidx]+1):
        countcoin(startidx+1, acc+coins[startidx]*i, cnt+i)

countcoin(0, 0, 0)
print(ans)