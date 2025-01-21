package 분할정복;

import java.util.Arrays;

public class 이진검색01_재귀 {

	static int[] arr = {8,9, 17, 19, 21, 23, 35, 88, 369};
	static int key = 19;
	
	public static void main(String[] args) {
		
		System.out.println(binarySearch(0, arr.length));
	}
	
	static boolean binarySearch(int left, int right) {
		// 기저 조건
		if(left>right) return false;
		// 재귀부분(중앙값이)
		int mid = (left+right)/2;
		// 같다면
		if(arr[mid]==key) return true;
		// 크다면
		else if(arr[mid]>key) return binarySearch(left, mid-1);
		//작다면
		else return binarySearch(mid+1, right);
	}
}
