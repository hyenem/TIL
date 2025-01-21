package 자료구조;

import java.util.Arrays;

import 자료구조.조합_01_재귀함수;

public class 부분집합_01_반복문 {
	
	static String[] 재료 = {"단무지", "햄", "오이", "시금치"};
	static int N = 4;
	static int[] sel = new int[N]; //해당 인덱스의 재료를 사용했는지의 유무를 지정하는 배열
	
	public static void main(String[] args) {
		// 재료가 4개! 반복문은 몇개?
		for(int i = 0; i<=1; i++) { // 단무지를 위한 반복문
			sel[0]=i;
			for(int j = 0; j<=1; j++) { // 햄을 위한 반복문
				sel[1]=j;
				for(int k = 0; k<=1; k++) { // 오이를 위한 반복문
					sel[2]=k;
					for(int l = 0; l<=1; l++) { // 시금치를 위한 반복문
						sel[3]=l;
						System.out.println(Arrays.toString(sel));
						// 눈으로 보고싶다.
						// for 문 하나 조건문과 결합해서 사용하면 무슨 김밥인지 알 수 있음.
					}
				}
			}
		}
	}
}
