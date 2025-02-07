T = int(input())
N, M = map(int, input().split())
# 각 피자에 번호 붙여주기
pizza = list(enumerate(map(int, input().split()), st))
print(pizza)
q = []

# 화덕에 피자 꽉 채우기
for i in range(N):
    q.append((i, pizza.pop(0)))
# 큐에 들어간 피자를 세는 것
ready
# 다 구워진 피자의 개수를 세는 것
done = 0
while cnt!=M:
    item = q.pop(0)
    if item//2==0:
        poppizza = item
        cnt+=1
        if pizza:
            q.append(())