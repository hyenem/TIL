package SWEA_5215_햄버거다이어트;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case=1; test_case<=T; test_case++) {
			int N = sc.nextInt();
			int L = sc.nextInt();
			
			int[] DP = new int[L+1];
			for(int i = 0; i<N; i++) {
				int score = sc.nextInt();
				int cal = sc.nextInt();
				for(int j = L; j>=cal; j--) {
					DP[j]=Math.max(DP[j], DP[j-cal]+score);
				}
			}
			System.out.println("#"+test_case+" "+DP[L]);
		}
	}
}
