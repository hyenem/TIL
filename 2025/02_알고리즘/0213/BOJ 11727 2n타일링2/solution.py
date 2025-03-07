N = int(input())
DP = [1, 1]+[0]*(N-1)
for i in range(2, N+1):
    # 마지막 한 칸을 세로로 세우는 경우와
    # 마지막 두 칸을 가로 2개, 2*2 1개로 채우는 경우의 합
    DP[i]=(DP[i-1]+DP[i-2]*2)%10007
print(DP[N])