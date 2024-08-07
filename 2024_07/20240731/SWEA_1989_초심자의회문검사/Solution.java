package SWEA_1989_초심자의회문검사;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int test_case = 1; test_case<T+1; test_case++) {
			String str = sc.next();
			int N = str.length();
			char[] arr = new char[N];
			for(int i =0; i<N; i++) {
				arr[i]=str.charAt(i);
			}
			int ans = 1;
			for (int i =0; i<N/2; i++) {
				if (arr[i]!=arr[N-1-i]) {
					ans = 0;
					break;
				}
			}
			
			System.out.println("#"+test_case+" "+ans);
		}
		
	}
}