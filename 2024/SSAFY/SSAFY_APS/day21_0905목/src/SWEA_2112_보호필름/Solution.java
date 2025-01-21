package SWEA_2112_보호필름;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case=1; test_case<=T; test_case++) {
			int D = sc.nextInt();
			int W = sc.nextInt();
			int K = sc.nextInt();
			
			int[][] arr = new int[D][W];
			int[][] connect = new int[D][W];
			
			for(int i = 0; i<D; i++) {
				for(int j = 0; j<W; j++) {
					arr[i][j]=sc.nextInt();
				}
			}
			
			int max = 0;
			for(int j = 0; j<W; j++) {
				int count = 1;
				for(int i = 1; i<D; i++) {
					if(arr[i-1][j]==arr[i][j]) count++;
					else count = 1;
					
					if (count==K) {
						max++;
						continue;
					}
				}
			}
			if(max>=K) {
				System.out.println("#"+test_case+" "+0);
				return;
			}
			
			for(int change = 0; change <=D; change++) {
				combination(change, 0, 0);
			}
			
		}
	}
	
	static void combination(int r, int count, int com) {
		if(count==r) {
			partition(com);
		}
	}
	
	static void partition(int com) {
		for(int i = )
	}
}
