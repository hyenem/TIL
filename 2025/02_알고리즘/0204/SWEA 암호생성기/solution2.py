# 주기성을 이횽하여 반복횟수 줄이기

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
    # 5와 q의 사이즈인 8이 서로소이므로
    # 5바퀴 돌 떄마다 모든 원소가 -1, -2, -3, -4, -5 가 이루어짐
    # 즉 5바퀴 돌 때마다 전체 원소가 10씩 감소함
    cicle = min(q)//10
    for i in range(8):
        q[i]-=cicle*10
    solution()
    print(f'#{tc}', *q)