package SWEA_1954_달팽이숫자;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for ( int test_case = 1; test_case<T+1; test_case++) {
			int N = sc.nextInt();
			int[][] arr = new int[N][N];
			
			int[] dx = {1,0,-1,0};
			int[] dy = {0,1,0,-1};
			
			int num = 1;
			int Switch = 0;
			int x = -1;
			int y = 0;
			for( int i = 2*N; i>1; i--) {
				for (int j = 0; j<i/2; j++) {
					x+=dx[Switch%4];
					y+=dy[Switch%4];
					arr[y][x]=num++;
				}
				Switch = (Switch+1)%4;
			}
			
            System.out.println("#"+test_case);
			for (int i=0; i<N; i++) {
				for (int j = 0; j<N; j++) {
					System.out.print(arr[i][j]+" ");
				}
				System.out.println();
			}
		}
	}
}
