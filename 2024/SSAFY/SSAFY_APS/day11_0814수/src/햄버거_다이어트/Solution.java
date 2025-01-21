package 햄버거_다이어트;

import java.util.Arrays;
import java.util.Scanner;

public class Solution {

	static int[] cal;
	static int[] score;
	static int N;
	static int L;
	static int ans;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1; test_case<=T; test_case++) {
			N= sc.nextInt();
			L = sc.nextInt();
			score = new int[N];
			cal = new int[N];
			for (int i = 0; i<N; i++) {
				score[i] = sc.nextInt();
				cal[i] = sc.nextInt();
			}

			ans = 0;
			for(int i = 0; i<N; i++) {
				calculate(i,0, 0);
			}
			System.out.println("#"+test_case+" "+ans);

		}
	}

	static void calculate(int start, int scoresum, int calsum) {
		if(start==N || calsum+cal[start]>L) {
			if(scoresum>ans) {
				ans = scoresum;
			}
			return;
		} else if (start==N-1) {
			scoresum+=score[start];
			if(scoresum>ans) {
				ans = scoresum;
			}
		}else {
			for(int i = start+1; i<N; i++) {
				calculate(i, scoresum+score[start], calsum+cal[start]);
			}
		}
	}
}
