package SWEA_7465_창용마을무리의개수;

import java.util.Scanner;

public class Solution {
	
	static int[] p;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case=1; test_case<=T; test_case++) {
			
			int N = sc.nextInt();
			int M = sc.nextInt();
			p = new int[N+1];
			for(int i = 0; i<N+1; i++) {
				p[i] = i;
			}
			
			for(int i = 0; i<M; i++) {
				int A = sc.nextInt();
				int B = sc.nextInt();
				p[findSet(B)]=findSet(A);
			}
			
			int count = 0;
			boolean[] visited = new boolean[N+1];
			for(int i = 1; i<N+1; i++) {
				if(visited[findSet(i)]) continue;
				count++;
				visited[findSet(i)]=true;
			}
			
			System.out.println("#"+test_case+" "+count);
		}
	}
	
	static int findSet(int x) {
		if(x!=p[x]) p[x] = findSet(p[x]);
		return p[x];
	}
}
