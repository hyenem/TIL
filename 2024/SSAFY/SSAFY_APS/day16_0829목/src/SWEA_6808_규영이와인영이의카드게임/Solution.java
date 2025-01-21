package SWEA_6808_규영이와인영이의카드게임;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Solution {
	
	static ArrayList<Integer> input;
	static ArrayList<Integer> other;
	static int[] result;
	static int ans = 0;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case=1; test_case<=T; test_case++) {
			input = new ArrayList<>();
			other = new ArrayList<>();
			
			for(int i = 0; i<9; i++) {
				input.add(sc.nextInt());
			}
			for(int i = 1; i<19; i++) {
				if(!input.contains(i))
				other.add(i);
			}

			int all = 1;
			for(int i = 2; i<10; i++) {
				all *= i;
			}
			
			ans = 0;
			result = new int[9];
			
			perm(0, 0);
			
			System.out.println("#"+test_case+" "+ans+" "+(all-ans));
			
		}
	}
	
	static void perm(int idx, int visited) {
		if(visited==(1<<9)-1) {
//			System.out.println(Arrays.toString(result));
			int sum = 0;
			for (int i = 0; i<9; i++) {
				if(result[i]<input.get(i)) sum+=result[i]+input.get(i);
				else sum-=result[i]+input.get(i);
			}
//			System.out.println(sum);
			if (sum>0) ans++;
			return;
		}
		for(int i = 0; i<9; i++) {
			if((visited&(1<<i))!=0) continue;
			result[idx]=other.get(i);
			perm(idx+1, visited|(1<<i));
		}
	}
}
