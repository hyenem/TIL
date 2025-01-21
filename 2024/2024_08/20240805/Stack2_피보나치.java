public class Stack2_피보나치 {
	public static void main(String[] args) {
		System.out.println(fibonacci2(45));
	}
	
	static int fibonacci(int N) {
		if(N<=1) return N;
		return fibonacci(N-1)+fibonacci(N-2);
	}
	
	static int fibonacci2(int N) {
		int[] arr = new int[N+1];
		arr[1]=1;
		for (int i = 2; i<=N; i++) {
			arr[i]=arr[i-1]+arr[i-2];
		}
		return arr[N];
	}
	
	static int[] dp = new int[500];
	static {
		dp[1]=1;
	}
	
	static int mFibo(int N) {
		if(N<=1) return 1;
		if(dp[N]!=0) return dp[N];
		return dp[N] = mFibo(N-1)+mFibo(N-2);
	}
}
