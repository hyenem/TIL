# 연산의 최솟값을 구하는 것이므로
# BFS를 사용하는 것이 효율적임

A, B = map(int, input().split())

# 필요한 연산의 개수+1, 지금 수
q = [(1, A)]

# 어차피 동작이 계속 증가하게 되어있으므로
# B보다 넘치면 의미 없으니까 사이즈 B
ans = -1

# 방문표시배열만들면 메모리 초과
# 어차피 뒤에 1을 붙이는 것은 홀수
# 두배를 하는 것은 짝수이므로
# 같은 곳을 두번 방문할 일이 아예 없음
while q:
    cnt, num = q.pop(0)
    if num*2==B or num*10+1==B:
        ans = cnt+1
        break
    if num*2<B:
        q.append((cnt+1, num*2))
    if num*10+1<B:
        q.append((cnt+1, num*10+1))
print(ans)