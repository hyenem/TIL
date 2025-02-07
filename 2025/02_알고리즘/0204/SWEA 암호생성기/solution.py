# 그냥 시키는대로 구현하기

# 이중 반복문 종료를 위한 함수화
def solution():
    while True:
        for i in range(1, 6):
            item = q.pop(0)
            if item-i<=0:
                q.append(0)
                return
            else :
                q.append(item-i)

for _ in range(10):
    tc = int(input())
    q = list(map(int, input().split()))
    solution()
    print(f'#{tc}', *q)