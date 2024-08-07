package SWEA1954_달팽이숫자;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int test_case = 1; test_case<T+1; test_case++) {
			int N = sc.nextInt();
			int[][] arr = new int[N][N];
			
			int num = 1;
			int x = 0;
			int y = -1;
			int[] dx = {0, 1, 0, -1};
			int[] dy = {1, 0, -1, 0};
			for (int i = 0; i<2*N-1; i++) {
				for (int j = (2*N-i)/2; j>0; j--) {
					x += dx[i%4];
					y += dy[i%4];
					arr[y][x]=num++;
				}
			}
			
			System.out.println("#"+test_case);
			for (int i = 0; i<N; i++) {
				for (int j = 0; j<N; j++) {
					System.out.print(arr[i][j]+" ");
				}
				System.out.println();
			}
		}
	}
}
