W = int(input())
arr=list(map(int, input().split()))
cost = [500, 100, 50, 10, 5, 1]
acc = [0]*6
cnt = [0]*6

# 나보다 저렴한 동전을 사용했을때 얼마까지 만들 수 있는지 계산
acc[5]=arr[5]*cost[5]
for i in range(4, -1, -1):
    acc[i] = acc[i+1]+arr[i]*cost[i]

# 나를 써야하는 만큼은 쓰고 다음으로 넘어가기
for i in range(5):
    cnt[i] = max(0, (W-(acc[i+1]+1))//cost[i]+1)
    W-=cnt[i]*cost[i]
cnt[5]=W

print(sum(cnt))
print(*cnt)