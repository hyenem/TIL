package 백트래킹;

import java.util.Scanner;

public class SWEA_5215_햄버거다이어트 {
	
	static int N, L;
	static int[] cals;
	static int[] scores;
	static int ans;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc = 1; tc <= T; tc++) {
			N = sc.nextInt();
			L = sc.nextInt();
			cals = new int[N];
			scores = new int[N];
			for(int i = 0; i<N; i++) {
				scores[i]=sc.nextInt();
				cals[i]=sc.nextInt();
			}//input끝
			
			ans=0;
			
			// 1. 비트 마스킹으로 풀 수 있다.
			makeBurger(0,0,0);
			System.out.println("#"+tc+" "+ans);
		}//tc
	}//main
	
	//중간결과를 들고다니겠다.
	static void makeBurger(int idx, int sumScore, int sumCal) {
		if(sumCal>L) return;
		//기저 조건
		if(idx==N) {
			// 모든 재료를 전부 다 고려헀어!
			if(ans < sumScore) {
				ans = sumScore;
			}
			return;
			// 베스트인지 아닌지 판단해라.
		}
		
		//재귀 부분
		// 이번에 idx 재료 사용 했다.
		makeBurger(idx+1, sumScore+scores[idx], sumCal+cals[idx]);
		//이번에 idx 재료를 사용하지 않았다.
		makeBurger(idx+1, sumScore, sumCal);
	}
}
