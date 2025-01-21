package SWEA_2115_벌꿀채취;

import java.util.ArrayList;
import java.util.Scanner;

public class Solution {

	static int N;
	static int M;
	static int C;
	static int ans;
	static ArrayList<Integer>[] listArr = new ArrayList[2];
	static int[][] arr;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1; test_case<=T; test_case++) {
			N = sc.nextInt();
			M = sc.nextInt();
			C = sc.nextInt();
			arr = new int[N][N];
			for(int i = 0; i<N; i++) {
				for(int j = 0; j<N; j++) {
					arr[i][j]=sc.nextInt();
				}
			}

			listArr[0]=new ArrayList<Integer>();
			listArr[1]=new ArrayList<Integer>();

			ans = 0;

		}
	}

	static void dfs(int i, int j, int sum, int count) {
		if(count==2) {
			// 두 명이 다 채집을 마쳤으면 이윤을 계산해서 최대값 업데이트
			
		}
		// 아직 두 명이 다 채집을 마치지 않았는데 모든 행을 다 썼으면 리턴
		if(i>=N) return;
		if (listArr[count].size()==M) {
			// 한 명이 M개를 다 채집했으면
			// 다음 사람으로 넘어감
			dfs(i, j, 0, count+1);
		} else if(j>=N) {
			// 아직 채집을 마치지 않았는데 열이 끝나면
			// 다음 줄로 내려가기
			listArr[count]=new ArrayList<Integer>();
			dfs(i+1, 0, 0, count);
		} else {
			dfs(i,j+1, sum, count);
			listArr[count].add(arr[i][j]);
			dfs(i, j+1, sum+arr[i][j], count);
			listArr[count].remove(listArr[count].size()-1);
		}
	}
}
