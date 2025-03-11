import math

# 8자리이므로 5자리까지 소수를 찾아둠
prime = [1]*100000
prime[1]=0
primenum = []

for i in range(2, 100000):
    if not prime[i]: continue
    primenum.append(i)
    for j in range(2*i, 100000, i):
        prime[j]=0

N = int(input())

# 한자리 소수
q = [2, 3, 5, 7]
# 한 번 반복할때마다 자리수가 하나씩 늘어남
for _ in range(N-1):

    nq = []
    for num in q:
        for i in (1, 3, 7, 9):
            next = num*10+i
            # 계산해둔 아이면 그거 참조
            if next<100000:
                if prime[next]:
                    nq.append(next)
                continue

            # 메모리 이슈로 게산 미리 못해두는 애들에 대해서
            # 루트까지 보고 소수면 다음 단계에 넣어주기
            for p in primenum:
                if p > math.sqrt(next):
                    nq.append(next)
                    break
                if next%p==0: break

    q = nq

for ele in q:
    print(ele)