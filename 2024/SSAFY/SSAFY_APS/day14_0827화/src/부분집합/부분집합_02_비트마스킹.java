package 자료구조;

import SWEA_4012_요리사.Solution;

public class 부분집합_02_비트마스킹 {
	
	static String[] 재료 = {"단무지", "햄", "오이", "시금치"};
	static int N = 4;
	static int[] sel = new int[N]; //해당 인덱스의 재료를 사용했는지의 유무를 지정하는 배열
	
	public static void main(String[] args) {

		// 2의 N승 만큼 반복한다.
		for(int i = 0; i<(1<<N); i++) {
			// 재료 확인 for문 필요하다.
			String tmp = "";
			for(int j = 0; j<N; j++) {
				if((i&(1<<j))>0) {
					// 해당 재료가 있어요~~
					tmp+=재료[j];
				}
			} // 재료확인 끝!
			System.out.println(tmp);
		}
		
	}
}
