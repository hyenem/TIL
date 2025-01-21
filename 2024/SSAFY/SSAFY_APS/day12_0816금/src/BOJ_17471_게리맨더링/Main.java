package BOJ_17471_게리맨더링;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static boolean[] team;
	static boolean[] checking;
	static int[] population;
	static int[][] adj;
	static int N;
	static int min;
	static boolean result;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		population = new int[N+1];
		for(int i = 1; i<N+1; i++) {
			population[i]=sc.nextInt();
		}

		adj = new int[N+1][];
		for(int i = 1; i<N+1; i++) {
			int[] row = new int[sc.nextInt()];
			for(int j = 0; j<row.length; j++) {
				row[j]=sc.nextInt();
			}
			adj[i]=row;
		}
		
		result = false;
		min = Integer.MAX_VALUE;
		for(int i =2; i<N; i++) {
			team = new boolean[N+1];
			combination(i);
		}
		if(!result) min = -1;
		System.out.println(min);

	}

	static void combination(int start) {
		if(start==N+1) {
			//전체 팀을 다 나누면 지역구 조건에 위배되지 않는지 채크하기
			checking = new boolean[N+1];
			check(1,0);
			return;
		}
		team[start]=true;
		for(int i = start; i<N+1; i++) {
			combination(i+1);
		}
		team[start]=false;
	}

	// 지역구가 잘 나눠졌는지 채크하기
	static void check(int start, int count) {
		System.out.println(start+" "+count);
		System.out.println(Arrays.toString(checking));
		if(count==2) {
			for(int i = 1; i<N+1; i++) {
				if(!checking[i]) return;
			}
			//지역구 조건에 하나도 위배 안되면 계산하기
			result = true;
			int sum = 0;
			for(int i = 1; i<N+1; i++) {
				if(team[i]) sum+=population[i];
				else sum-=population[i];
			}
			min = Math.min(min, Math.abs(sum));
			System.out.println("calculate: "+min);
			return;
		}
		if(start == N+1) return;
		if(start < N+1) {
			checking[start]=true;
			for(int i = 0; i<adj[start].length;i++) {
				if(!checking[adj[start][i]] && team[adj[start][i]]==team[start])
					check(adj[start][i], count);
					System.out.println("next"+ adj[start][i]);
			}
			for(int i = start; i<N; i++) {
				if(!checking[i+1]) check(i+1, count+1);
			}
			checking[start]=false;
			
		}
	}
}
