package 그래프DFSBFS;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class 그래프최소비용01_크루스칼 {
	
	static class Edge implements Comparable<Edge>{
		int A, B, W;

		public Edge(int a, int b, int w) {
			super();
			A = a;
			B = b;
			W = w;
		}

		@Override
		public String toString() {
			return "Edge [A=" + A + ", B=" + B + ", W=" + W + "]";
		}

		@Override
		public int compareTo(Edge o) {
			return this.W - o.W;
//			return Integer.compare(this.W, o.W);
		}
	}
	static int[] p; // 대표자를 저장할 배열
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int V = sc.nextInt(); // 정점의 개수(정점의 시작번호를 보고)
		int E = sc.nextInt(); // 간선의 개수
		
		Edge[] edges = new Edge[E];
		for(int i = 0; i<E; i++) {
			int A = sc.nextInt();
			int B = sc.nextInt();
			int W = sc.nextInt();
			edges[i] = new Edge(A, B, W);
		} // 입력 끝
		
		//크루스칼 제 1장 : 가중치 순으로 정렬을 해라!
//		1. comparator로
//		Arrays.sort(edges, new Comparator<Edge>() {
//
//			@Override
//			public int compare(Edge o1, Edge o2) {
//				// TODO Auto-generated method stub
//				return o1.W - o2.W;
//			}
//			
//		});
		
//		2. comparable, compareTo
		Arrays.sort(edges);
		
		//크루스칼 제 2장 : V-1개의 간선을 뽑아라! (사이클이 발생하지 않게)
		//상호배타집합(서로소 집합, 유니온파인드)
		p = new int[V];
		
		//make-set을 통해 전체 자신을 대표로 만드는 작업을 수행한다.
		for(int i = 0; i<V; i++) {
			p[i]=i;
//			makeSet(i);
		}
		
		int ans = 0; //최소 비용을 저장하기 위한 변수
		int pick = 0; // 내가 뽑은 간선의 개수
		
		for(int i = 0; i<E; i++) {
			int x = edges[i].A;
			int y = edges[i].B;
			
//			//사이클이 발생하는지 검사를 해야한다.
//			if(findSet(x)!=findSet(y)) {
//				// 해당 블록에 들어왔다면 사클이 아니라는 뜻
//				union(x, y);
//				ans += edges[i].W;
//				pick++;
//			}
			
			
			//findSet 호출 횟수 줄여보면?
			int px = findSet(edges[i].A);
			int py = findSet(edges[i].B);
			if(px!=py) {
				union(px, py);
				ans += edges[i].W;
				pick++;
			}
			if(pick==(V-1)) break;
		}
	}//main
	
	static void makeSet(int x) {
		p[x]=x;
	}
	
	static int findSet(int x) {
//		if(x==p[x]) return x;
//		return findSet(p[x]);
//		
		//위의 코드는 똑같은 작업을 반복 수행해서 효율이 떨어짐
		if(x!=p[x]) p[x]=findSet(p[x]);
		return p[x];
	}
	
	static void union(int x, int y) {
		// x와 y는 대표자여야만 한다.
		p[findSet(y)]=findSet(x);
	}
}
