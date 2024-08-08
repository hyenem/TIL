package SWEA_1974_스도쿠검증;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		end: for (int test_case = 1; test_case<=T; test_case++) {
			int[][] arr = new int[9][9];
			boolean[] visited = new boolean[10];
			
			for (int i = 0; i<9; i++) {
				for (int j =0; j<9; j++) {
					arr[i][j]=sc.nextInt();
				}
			}
			
			for (int i = 0; i<9; i++) {
				//가로검사
				visited = new boolean[10];
				for (int j = 0; j<9; j++) {
					if(visited[arr[i][j]]) {
						System.out.println("#"+test_case+" "+0);
						continue end;
					}
					visited[arr[i][j]]=true;
				}
				
				//세로검사
				visited = new boolean[10];
				for (int j = 0; j<9; j++) {
					if(visited[arr[j][i]]) {
						System.out.println("#"+test_case+" "+0);
						continue end;
					}
					visited[arr[j][i]]=true;
				}
			}
			
			for(int i = 0; i<9; i++) {
				visited = new boolean[10];
				for (int j = 0; j<9; j++) {
					if(visited[arr[(i%3)*3+j%3][(i/3)*3+j/3]]) {
						System.out.println("#"+test_case+" "+0);
						continue end;
					}
					visited[arr[(i%3)*3+j%3][(i/3)*3+j/3]]=true;
				}
			}
			System.out.println("#"+test_case+" "+1);
		}
	}
}