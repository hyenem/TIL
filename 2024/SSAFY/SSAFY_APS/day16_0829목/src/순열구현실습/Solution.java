package 순열구현실습;

import java.util.Arrays;

public class Solution {
	
	static int[] nums;
	static int N;
	
	public static void main(String[] args) {
		nums = new int[] {1,2,3};
		N = nums.length;
		
//		perm1();
//		perm2(0);
		
		visited = new boolean[N];
		result = new int[N];
//		perm3(0);
		
		perm4(0,0);
		
	}
	
	//반복문
	static void perm1() {
		for(int i = 0; i<N; i++) {
			for(int j = 0; j<N; j++) {
				if(i!=j) {
					for(int k = 0; k<N; k++) {
						if(i!=k&& j!=k) System.out.println(nums[i]+" "+nums[j]+" "+nums[k]);
					}
				}
			}
		}
	}
	
	//swap
	static void swap(int i, int j) {
		int tmp = nums[i];
		nums[i] = nums[j];
		nums[j] = tmp;
	}
	static void perm2(int idx) {
		if(idx==N) {
			System.out.println(Arrays.toString(nums));
		}
		for(int i = idx; i<N; i++) {
			swap(i, idx);
			perm2(idx+1);
			swap(i, idx);
		}
	}
	
	//방문채크
	static boolean[] visited;
	static int[] result;
	
	static void perm3(int idx) {
		if(idx==N) {
			System.out.println(Arrays.toString(result));
			return;
		}
		for(int i = 0; i<N; i++) {
			if(visited[i]) continue;
			result[idx]=nums[i];
			visited[i]=true;
			perm3(idx+1);
			visited[i]=false;
		}
	}
	
	//비트마스크
	static void perm4(int idx, int visited) {
		if(visited==(1<<N)-1) {
			System.out.println(Arrays.toString(result));
			return;
		}
		for(int i = 0; i<N; i++) {
			if((visited&(1<<i))!=0) continue;
			result[idx]=nums[i];
			perm4(idx+1, visited|(1<<i));
		}
	}
	
	
}
