package SWEA_13501_수열편집;

import java.util.LinkedList;
import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case=1; test_case<=T; test_case++) {
			int N =sc.nextInt();
			int M = sc.nextInt();
			int L = sc.nextInt();
			
			LinkedList<Integer> list = new LinkedList<>();
			for(int i = 0; i<N; i++) {
				list.add(sc.nextInt());
			}
			
			for(int i = 0; i<M; i++) {
				char now = sc.next().charAt(0);
				if(now=='I') {
					list.add(sc.nextInt(), sc.nextInt());
				} else if (now=='D') {
					list.remove(sc.nextInt());
				} else {
					int idx = sc.nextInt();
					list.remove(idx);
					list.add(idx, sc.nextInt());
				}
			}
			
			System.out.print("#"+test_case+" ");
			if(list.size()<=L) System.out.println(-1);
			else System.out.println(list.get(L));
		}
	}
}
