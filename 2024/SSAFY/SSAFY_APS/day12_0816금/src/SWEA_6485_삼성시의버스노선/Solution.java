package SWEA_6485_삼성시의버스노선;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T =sc.nextInt();
		for(int test_case = 1; test_case<=T; test_case++) {
			int[] busStop = new int[5001];
			int N = sc.nextInt();
			for(int i = 0; i<N; i++) {
				int A = sc.nextInt();
				int B = sc.nextInt();
				for(int j = A; j<=B; j++) {
					busStop[j]++;
				}
			}
			
			int P = sc.nextInt();
			System.out.print("#"+test_case);
			for(int i = 0; i<P; i++) {
				System.out.print(" "+busStop[sc.nextInt()]);
			}
			System.out.println();
		}
	}
}
