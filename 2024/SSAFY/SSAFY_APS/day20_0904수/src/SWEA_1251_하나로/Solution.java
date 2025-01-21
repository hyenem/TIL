package SWEA_1251_하나로;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Solution {
	
	static class Edge implements Comparable<Edge> {
		int A, B;
		double W;
		
		public Edge(int a, int b, double w) {
			super();
			A = a;
			B = b;
			W = w;
		}

		@Override
		public int compareTo(Edge o) {
			return Double.compare(this.W, o.W);
		}
	}
	
	static int[] p;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case=1; test_case<=T; test_case++) {
			int N = sc.nextInt();
			long[] X = new long[N];
			long[] Y = new long[N];
			for(int i = 0; i<N; i++) {
				X[i]=sc.nextLong();
			}
			for(int i = 0; i<N; i++) {
				Y[i]=sc.nextLong();
			}
			double E = sc.nextDouble();
			
			ArrayList<Edge> edges = new ArrayList<>();
			
			for(int i = 0; i<N-1; i++) {
				for(int j = i+1; j<N; j++) {
					long L2 = (X[i]-X[j])*(X[i]-X[j]) + (Y[i]-Y[j])*(Y[i]-Y[j]);
					double W = E * L2;
					edges.add(new Edge(i, j, W));
				}
			}
			
			Collections.sort(edges);
			
			p = new int[N];
			for(int i = 0; i<N; i++) {
				p[i]=i;
			}
			
			double ans = 0;
			int count = 0;
			for(int i = 0; i<edges.size(); i++) {
				int A = edges.get(i).A;
				int B = edges.get(i).B;
				
				int pa = findSet(A);
				int pb = findSet(B);
				
				if(pa!=pb) {
					p[pa]=pb;
					ans+=edges.get(i).W;
					count++;
				}
				
				if(count==N-1) break;
			}
			
			System.out.printf("#%d %.0f\n", test_case, ans);
		}
	}
	
	static int findSet(int x) {
		if(x!=p[x]) p[x]=findSet(p[x]);
		return p[x];
	}
}
