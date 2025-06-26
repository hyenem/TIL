package BOJ1949_우수마을;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
	
	static List<Integer>[] adj;
	static int[][] DP;
	static int[] population;
	
	public static void calmax(int r) {
		
		System.out.println(r);
		System.out.println(Arrays.deepToString(DP));
		
		DP[r][0]=0;
		DP[r][1]=population[r];
		
		int mindist = -1;
		boolean allbad = true;
		boolean leaf = true;
		
		for(int v : adj[r]) {
			if(DP[v][0]!=-1) continue;
			leaf = false;
			calmax(v);
			
			// r이 우수마을인 경우
			DP[r][1] += DP[v][0];
			
			// r이 우수마을이 아닌 경우
			if(DP[v][0]<=DP[v][1]) {
				allbad = false;
				DP[r][0] += DP[v][1];
			} else {
				DP[r][0] += DP[v][0];
				if(mindist == -1) {
					mindist = DP[v][2];
				} else if (DP[v][2]<mindist) {
					mindist = DP[v][2];
				}
			}
			
		}
		
		// r이 우수마을이 아닌 경우 중 자식 중 하나라도 우수마을인 경우
		DP[r][3] = DP[r][0];
		if(!leaf && allbad) DP[r][3] -= mindist;
		
		DP[r][2] = Math.abs(DP[r][0]-DP[r][1]);
		System.out.println(Arrays.deepToString(DP));
		
	}
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		population = new int[N+1];
		for(int i = 1; i<=N; i++) {
			population[i] = sc.nextInt();
		}
		
		adj = new List[N+1];
		DP = new int[N+1][4];
		for(int i = 0; i<=N; i++) {
			DP[i][0]=-1;
			DP[i][1]=-1;
			DP[i][2]=-1;
			DP[i][3]=-1;
		}
		
		
		for(int i = 0; i<=N; i++) {
			adj[i] = new ArrayList<>();
		}
		
		for(int i = 0; i<N-1; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			adj[a].add(b);
			adj[b].add(a);
		}
				
		calmax(1);
		System.out.println(Arrays.deepToString(DP));
		System.out.println(Math.max(DP[1][0], DP[1][1]));
	}

}
