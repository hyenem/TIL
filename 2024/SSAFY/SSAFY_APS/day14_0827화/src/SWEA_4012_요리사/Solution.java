package SWEA_4012_요리사;

import java.util.Arrays;
import java.util.Scanner;

public class Solution {
	
	static int N;
	static int[][] arr;
	static int ans;
	static boolean[] team;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case=1; test_case<=T; test_case++) {
			N = sc.nextInt();
			arr = new int[N][N];
			for(int i = 0; i<N; i++) {
				for(int j = 0; j<N; j++) {
					arr[i][j]=sc.nextInt();
				}
			}
			
			ans=Integer.MAX_VALUE;
			team = new boolean[N];
			combination(1,0);
			
			System.out.println("#"+test_case+" "+ans);
		}
	}
	
	static void combination(int idx, int count) {
		if(count==N/2) {
			int sum = 0;
			for(int i = 0; i<N; i++) {
				for(int j = 0; j<N; j++) {
					if(team[i] && team[j]) {
						sum-=arr[i][j];
					} else if (!team[i]&&!team[j]) {
						sum+=arr[i][j];
					}
				}
			}
			ans = Math.min(ans, Math.abs(sum));
			return;
		}
		if(idx==N) return;
		for(int i = idx; i<N; i++) {
			team[i]=true;
			combination(i+1, count+1);
			team[i]=false;
		}
	}
}
