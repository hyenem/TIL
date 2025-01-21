package 요리사;

import java.util.Scanner;

public class Solution {
	
	static boolean[] team;
	static int[][] arr;
	static int N;
	static int min;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//테스트 케이스 개수	
		int T = sc.nextInt();
		for (int test_case = 1; test_case<=T; test_case++) {
			//식재료 개수
			N = sc.nextInt();
			//식재료 배열
			arr = new int[N][N];
			for(int i = 0; i<N; i++) {
				for (int j=0; j<N; j++) {
					arr[i][j]=sc.nextInt();
				}
			}
			//식재료를 둘로 나누기 위한 배열
			team = new boolean[N];
			//첫번쨰 재료는 우선 한 팀에 넣어둠
			team[0]=true;
			min = Integer.MAX_VALUE;
			combination(1, 1);
			
			System.out.println("#"+test_case+" "+min);
			
		}
	}
	
	// 팀을 정하기 위한 
	static void combination(int start, int count) {
		// 팀을 정확하게 나누면 계산하기
		if(count==N/2) {
			int sum = 0;
			for (int i = 0; i<N; i++) {
				for (int j = i+1; j<N; j++) {
					if(team[i]&&team[j]) {
						sum+=arr[i][j];
						sum+=arr[j][i];
					} else if(!team[i]&&!team[j]) {
						sum-=arr[i][j];
						sum-=arr[j][i];
					}
				}
			}
			sum = Math.abs(sum);
			if(min>sum) min = sum;
		} else {
			for(int i = start; i<N; i++) {
				team[i]=true;
				combination(i+1, count+1);
				team[i]=false;
			}
		}
	}
}