package SWEA_5215_햄버거다이어트;

import java.util.Scanner;

public class Solution_2 {
	
	static int[][] arr;
	static int ans;
	static int N, L;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case=1; test_case<=T; test_case++) {
			N = sc.nextInt();
			L = sc.nextInt();
			
			arr = new int[N][2];
			for(int i = 0; i<N; i++) {
				arr[i]= new int[]{sc.nextInt(), sc.nextInt()};
			}
			
			ans = 0;
			for(int i=0; i<N; i++) {				
				combination(i,0,0);
			}
			
			System.out.println("#"+test_case+" "+ans);
		}
	}
	
	static void combination(int start, int sumcal, int sumscore) {
		if(sumcal+arr[start][1]>L) {
			ans = Math.max(ans, sumscore);
			return;
		}
		for(int i=start; i<N; i++) {
			combination(i+1, sumcal+arr[start][1], sumscore+arr[start][0]);
		}
	}
}
