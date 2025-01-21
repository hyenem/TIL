package SWEA_1231_중위순회;

import java.util.Arrays;
import java.util.Scanner;
import java.util.TreeSet;

public class Solution {
	static char[] data;
	static int[][] child;
	static int N;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for(int test_case=1; test_case<=10; test_case++) {
			N = sc.nextInt();
			data = new char[N+1];
			child = new int[2][N+1];
			for(int i = 0; i<N; i++) {
				int nowidx = sc.nextInt();
				data[nowidx]=sc.next().charAt(0);
				String str = sc.nextLine();
				int count = 0;
				int tmpint = 0;
				if(str.length()==0) continue;
				for(int j = 1; j<str.length(); j++) {
					if(str.charAt(j)==' ') {
						child[count][nowidx]=tmpint;
						count++;
						tmpint=0;
					} else {
						tmpint = tmpint*10 + str.charAt(j)-'0';
						if(j==str.length()-1) {
							child[count][nowidx]=tmpint;
							count++;
						}
					}
				}
			}
			System.out.print("#"+test_case+" ");
			inorder(1);
			System.out.println();
		}
	}
	
	static void inorder(int root) {
		if(root>N || root==0) return;
		inorder(child[0][root]);
		System.out.print(data[root]);
		inorder(child[1][root]);
	}
}