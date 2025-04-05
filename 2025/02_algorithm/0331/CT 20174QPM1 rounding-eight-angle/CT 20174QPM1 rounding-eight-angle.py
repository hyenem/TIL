'''2회독
제출횟수 : 1회
풀이시간 : 15분

* 1BASED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
* 맵이 주어진게 아니라 숫자가 주어졌을땐 0시작, 1시작 꼭 채크하기

* 코드 로직은 1회독이랑 거의 똑같다
* for문 while문 차이 정도?
'''

arr = [list(map(int, input())) for _ in range(4)]
idx = [0]*4
K = int(input())
cmds = [tuple(map(int, input().split())) for _ in range(K)]

for n, d in cmds:
    n -= 1
    left, right = n-1, n+1
    while left>=0 and arr[left][(idx[left]+2)%8]!=arr[left+1][(idx[left+1]-2)%8]:
        left -= 1
    left += 1
    while right<4 and arr[right][(idx[right]-2)%8]!=arr[right-1][(idx[right-1]+2)%8]:
        right += 1
    right -= 1

    for i in range(left, right+1):
        idx[i] = (idx[i]+(-1)**(abs(i-n)+1)*d)%8

ans = 0
for i in range(4):
    ans += (2**i)*arr[i][idx[i]]
print(ans)

'''1회독
c = [list(map(int, input())) for _ in range(4)]
# 12시방향을 나타내는 포인터
# 시계방향으로 돌면 포인터에서 1을 빼주고
# 반시계방향으로 돌면 포인터에서 1을 더해주면 됨
p = [0]*4

K = int(input())
for _ in range(K):
    idx, dir = map(int, input().split())
    idx -= 1
    dir *= -1

		# 기존 상황을 저장하고
		# tmp 를 이용하여 비교하여 p를 업데이트
    tmp = p[:]
    
    # 제일 처음 톱니바퀴를 돌리고
    p[idx] = (p[idx]+dir)%8
    
    # 왼쪽으로 가면서 돌릴 수 있을 만큼 돌리기
    if idx!=0:
        for i in range(idx-1, -1, -1):
            if c[i][(tmp[i]+2)%8]!=c[i+1][(tmp[i+1]-2)%8]:
                p[i]=(p[i]+dir*((-1)**(idx-i)))%8
            else :
                break
                
    # 오른쪽으로 가면서 돌릴 수 있을 만큼 돌리기
    if idx!=3:
        for i in range(idx+1, 4, 1):
            if c[i][(tmp[i]-2)%8]!=c[i-1][(tmp[i-1]+2)%8]:
                p[i]=(p[i]+dir*((-1)**(i-idx)))%8
            else :
                break
                
print(c[0][p[0]]+2*c[1][p[1]]+4*c[2][p[2]]+8*c[3][p[3]])
'''