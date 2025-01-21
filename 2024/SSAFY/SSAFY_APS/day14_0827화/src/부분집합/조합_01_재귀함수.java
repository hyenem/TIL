package 자료구조;

import java.util.Arrays;

public class 조합_01_재귀함수 {
	
	static String[] 재료 = {"상추", "패티", "치즈", "토마토"};
	static int N, R; // N: 재료의 수, R: 내가 뽑고 싶은 재료의 수
	static String[] sel; // 뽑은 재료들을 저장할 배열
	
	public static void main(String[] args) {
		N=4;
		R=2;
		sel = new String[R];
		
		combination(0,0);
		
	}
	
	// idx : 재료의 인덱스
	// sidx : 뽑은 재료의 인덱스
	private static void combination(int idx, int sidx) {
		if(sidx==R) {
			System.out.println(Arrays.toString(sel));
			return;
		}
		if(idx==N) {
			return;
		}
		// 해당 idx 번째 재료를 사용 했는지, 안했는지
		sel[sidx]=재료[idx];
		combination(idx+1, sidx+1);
		combination(idx+1, sidx);
	}
}
