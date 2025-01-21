package SWEA_1860_진기의최고급붕어빵;

import java.util.Arrays;
import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T =sc.nextInt();
		for (int test_case = 1; test_case<=T; test_case++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			int K = sc.nextInt();
			
			int[] arr = new int[N];
			for (int i = 0; i<N; i++) {
				arr[i]=sc.nextInt();
			}
			Arrays.sort(arr);
			
			String result="Possible";
			for(int i = 0; i<N; i++) {
				if((arr[i]/M)*K-i<=0) {
					result = "Impossible";
				}
			}
			System.out.println("#"+test_case+" "+result);
		}
	}
}