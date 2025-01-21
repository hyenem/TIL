package SWEA_1248_공통조상;

import java.util.ArrayList;
import java.util.Scanner;

public class Solution {
	
	static int subtree;
	static int V;
	static int[][] child;
	static int[] parent;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int test_case = 1; test_case<=T; test_case++) {
			V = sc.nextInt();
			int E = sc.nextInt();
			int num1 = sc.nextInt();
			int num2 = sc.nextInt();
			
			child = new int[2][V+1];
			parent = new int[V+1];
			for (int i =0; i<E; i++) {
				int p_idx = sc.nextInt();
				int c_idx = sc.nextInt();
				
				if(child[0][p_idx]!=0) child[1][p_idx]=c_idx;
				else child[0][p_idx]=c_idx;
				
				parent[c_idx]=p_idx;
			}
			
			ArrayList<Integer> num1_list = new ArrayList<>();
			int num1_parent = parent[num1];
			while(num1_parent!=1) {
				num1_list.add(num1_parent);
				num1_parent = parent[num1_parent];
			}
			num1_list.add(1);
			
			int common = num2;
			while (true) {
				if(num1_list.contains(common)) break;
				common = parent[common];
			}
			
			subtree = 0;
			count(common);
			
			System.out.println("#"+test_case+" "+common+" "+subtree);
			
			
			
		}
	}
	
	static void count(int root) {
		if(root>V || (root!=1 && parent[root]==0)) return;
		count(child[0][root]);
		count(child[1][root]);
		subtree++;
	}
}