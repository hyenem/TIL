package 백트래킹;

import java.util.Arrays;

public class 순열03_방문채크 {
	static int[] nums;
	static int N;
	//추가적인 공간 필요
	static boolean[] visited;
	static int[] result;
	
	public static void main(String[] args) {
		nums = new int[] {1,2,3};
		N = nums.length;
		visited = new boolean[N];
		result = new int[N];
		
		perm(0);
		
	}//main
	
	static void perm(int idx) {
		//기저조건
		if(idx==N) {
			System.out.println(Arrays.toString(result));
			return;
		}
		// 재귀부분
		for(int i = 0; i<N; i++) {
			//사용하지 않은 원소를 가지고 만들어야해
			if(visited[i]) continue;
			result[idx] = nums[i];
			visited[i]=true;
			perm(idx+1);
			visited[i]=false;
		}
	}
}
