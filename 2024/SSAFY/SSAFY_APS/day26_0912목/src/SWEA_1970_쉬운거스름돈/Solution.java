package SWEA_1970_쉬운거스름돈;

import java.util.Arrays;
import java.util.Scanner;

public class Solution {
	static int[] coin = {1, 5, 10, 50, 100, 500, 1000, 5000};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc = 1; tc<=T; tc++) {
			int N = sc.nextInt()/10;
			int[][] arr = new int[3][N+1];
			Arrays.fill(arr[0], Integer.MAX_VALUE);
			arr[0][0]=0;
			
			
			for(int i = 1; i<=N; i++) {
				for(int j=0; j<8; j++) {
					if(i>=coin[j]) {
						if(arr[0][i-coin[j]]+1>=0 && arr[0][i]>arr[0][i-coin[j]]+1) {
							arr[0][i]=arr[0][i-coin[j]]+1;
							arr[1][i]=i-coin[j];
							arr[2][i]=j;
						}
					}
				}
			}
			
			int[] ans = new int[8];
			int now = N;
			while(now != 0) {
				ans[arr[2][now]]++;
				now = arr[1][now];
			}
			
			System.out.println("#"+tc);
			for(int i = 7; i>=0; i--) {
				System.out.print(ans[i]+" ");
			}
			System.out.println();
		}
	}
}
