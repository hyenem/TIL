package 백트래킹;

import java.util.Arrays;

public class 순열02_SWAP {
	static int[] nums;
	static int N;
	
	public static void main(String[] args) {
		nums = new int[] {1,2,3};
		N = nums.length;
		
		perm(0);
		
	}//main
	
	//idx:현재 판단 위치
	static void perm (int idx) {
		//기저조건
		if(idx==N) {
			System.out.println(Arrays.toString(nums));
			return;
		}
		
		//재귀부분
		for(int i = idx; i<N; i++) {
			swap(i, idx);
			perm(idx+1);
			swap(i, idx);
		}
	}
	
	//바꾸고 싶은 배열이 static하게 선언이 되어있으니 위치 2개만 인자로 보내겠다.
	static void swap(int a, int b) {
		int tmp = nums[a];
		nums[a]=nums[b];
		nums[b]=tmp;
	}
}
