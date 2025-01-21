package SWEA_21885_신입사원분반교육;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case=1; test_case<=T; test_case++) {
			int N = sc.nextInt();
			int min = sc.nextInt();
			int max = sc.nextInt();
			
			int[] score = new int[101];
			int sum = 0;
			for(int i = 0; i<N; i++) {
				score[sc.nextInt()]++;
			}
			
			int ans = Integer.MAX_VALUE;
			boolean result=false;
			int team1=0;
			int team2=0;
			int team3=0;
			for(int score1=0; score1<101; score1++) {
				for(int score2 = score1+1; score2<101; score2++) {
					team1=0;
					team2=0;
					team3=0;
					for(int k = 0; k<score1; k++) {
						team1+=score[k];
					}
					for(int k = score1; k<score2; k++) {
						team2+=score[k];
					}
					team3 = N-team1-team2;
					
					if(team1<min||team2<min||team3<min||
							team1>max||team2>max||team3>max) {
						continue;
					}
					result = true;
					int nowmin = Math.min(Math.min(team1, team2),team3);
					int nowmax = Math.max(Math.max(team1, team2),team3);
					ans = Math.min(ans, nowmax-nowmin);
				}
			}
			
			if(!result) ans=-1;
			System.out.println("#"+test_case+" "+ans);
		}
		
	}
}
