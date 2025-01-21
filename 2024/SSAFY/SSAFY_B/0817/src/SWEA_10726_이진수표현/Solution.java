package SWEA_10726_이진수표현;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1; test_case<=T; test_case++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			String ans="OFF";
			M%=Math.pow(2, N);
			if(M==Math.pow(2,N)-1) ans="ON";
			
			System.out.println("#"+test_case+" "+ans);
		}
	}
}
