package SWEA_2001_파리퇴치;

import java.util.Scanner;

public class Solution {
	
	static int[][] arr;
	static int M;
	static int max;
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for (int test_case = 1; test_case<T+1; test_case++) {
			int N = sc.nextInt();
			M = sc.nextInt();
			arr = new int[N][N];
			for (int i = 0; i<N; i++) {
				for (int j = 0; j<N; j++) {
					arr[i][j]=sc.nextInt();
				}
			}
			
			max = 0;
			for (int i = 0; i <N+1-M; i++) {
				for (int j = 0; j<N+1-M; j++) {
					fly(i,j);
				}
			}
			
			System.out.println("#"+test_case+" "+max);
		}
	}
	
	static void fly(int i, int j) {
		int sum = 0;
		for (int k = 0; k<M; k++) {
			for(int l = 0; l<M; l++) {
				sum+=arr[i+k][j+l];
			}
		}
		max = Math.max(max, sum);
	}
}