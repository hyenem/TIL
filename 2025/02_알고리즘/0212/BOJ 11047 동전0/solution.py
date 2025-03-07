N, K = map(int,input().split())
stack = []
for _ in range(N):
    num = int(input())
    # K보다 큰 동전은 쓸일이 없다
    if num>K:
        break
    stack.append(num)

ans = 0
while K != 0:
    # 가장 큰 동전부터 쓸수 있는만큼 다스기
    num = stack.pop()
    ans += K//num
    K = K%num

print(ans)