package SWEA_2001_파리퇴치;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1; test_case<T+1; test_case++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			int[][] arr = new int[N][N];
			for (int i = 0; i<N; i++) {
				for (int j = 0; j<N; j++) {
					arr[i][j]=sc.nextInt();
				}
			}
			
			int max = 0;
			for(int i = 0; i<N-M+1; i++) {
				for (int j = 0; j<N-M+1; j++) {
					int sum = 0;
					for (int k1 = 0; k1<M; k1++) {
						for (int k2 = 0; k2<M; k2++) {
							sum += arr[i+k1][j+k2];
						}
					}
					if (max<sum) max = sum;
				}
			}
			System.out.println("#"+test_case+" "+max);
		}
	}
}