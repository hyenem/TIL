package CT3;

import java.util.Arrays;
import java.util.Scanner;

public class 동적계획법01_피보나치 {
	
	static int[] callFibo = new int[1000];
	static int[] memo;
	
	static {
		memo = new int[1000];
		Arrays.fill(memo, -1);
		memo[0]=0;
		memo[1]=1;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		System.out.println(fibo1(N));
		System.out.println(fibo2(N));
		System.out.println(fibo3(N));
//		System.out.println(Arrays.toString(callFibo));
	}
	
	static int fibo1(int n) {
		callFibo[n]++;
		//기저조건 n==0 : 0을 반환, n==1 : 1을 반환
		if(n<=1) return n;
		return fibo1(n-1)+fibo1(n-2);
	}
	
	static int fibo2(int n) {
		if(memo[n]==-1)
			memo[n]=fibo2(n-1)+fibo2(n-2);
		return memo[n];
	}
	
	static int fibo3(int n) {
		int[] dp = new int[n+1];
		dp[0]=0;
		dp[1]=1;
		for(int i = 2; i<=n; i++) {
			dp[i]=dp[i-1]+dp[i-2];
		}
		return dp[n];
	}
}
