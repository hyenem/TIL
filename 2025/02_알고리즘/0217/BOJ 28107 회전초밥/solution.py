import heapq

N, M = map(int, input().split())
q = []

# 누가 뭘 먹고싶은지 우선순위 큐에 넣기
# 사람 번호가 빠를수록 빨리 뽑히도록
for i in range(N):
    K, *tmp = map(int, input().split())
    for ele in tmp:
        heapq.heappush(q, (i, ele))

# 스시 개수 저장
sushi = [0]*200001
for ele in map(int, input().split()):
    sushi[ele]+=1

ans = [0]*N
while q:
    # 어떤 사람이 무슨 스시
    p, s = heapq.heappop(q)
    # 해당 스시가 안남으면 넘어가기
    if sushi[s]==0:
        continue
    # 남았으면 스시 하나 줄이고 답 하나늘리고
    sushi[s]-=1
    ans[p]+=1

print(*ans)