package SWEA_2806_NQueen;

import java.util.Scanner;

public class Solution {
	
	static int N;
	static int ans;
	static int[] queen;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case=1; test_case<=T; test_case++) {
			N = sc.nextInt();
			ans = 0;
			queen = new int[N];
			
			turn(0);
			
			System.out.println("#"+test_case+" "+ans);
		}
	}
	
	static void turn(int idx) {
		if(idx == N) {
			ans++;
			return;
		}
		end : for(int i=0; i<N; i++) {
			for(int j = 0; j<idx; j++) {
				if(queen[j]==i) continue end;
				if(Math.abs(queen[j]-i)==Math.abs(j-idx)) continue end;
			}
			queen[idx]=i;
			turn(idx+1);
		}
	}
}
