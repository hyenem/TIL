package 백트래킹;

import java.util.ArrayList;
import java.util.Arrays;

public class 순열04_비트마스크 {
	static int[] nums;
	static int N;
	//추가적인 공간 필요
	static int[] result;
	static ArrayList<int[]> list;
	
	public static void main(String[] args) {
		nums = new int[] {1,2,3};
		N = nums.length;
		result = new int[N];
		list = new ArrayList<>();
		
		perm(0, 0);
		//결과를 모아서 볼고 했을 때 잘 해야한다
		// 이슈가 생길 수 있음
		for(int[] arr : list) {
			System.out.println(Arrays.toString(arr));
		}
	}//main
	
	//visited : 사용한 원소를 저장하기 위한 정수
	static void perm(int idx, int visited) {
		//기저조건
		if(visited==(1<<N)-1) {
			int[] thisresult = new int[N];
			for(int i = 0; i<N; i++) {
				thisresult[i]=result[i];
			}
			list.add(thisresult);
			return;
		}
		// 재귀부분
		for(int i = 0; i<N; i++) {
			if((visited&(1<<i))!=0) continue;
			result[idx]=nums[i];
			perm(idx+1, visited|(1<<i));
		}
	}
}
