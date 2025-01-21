package 퀵정렬구현;

import java.util.Arrays;

public class Solution {

	static int[] arr = {29, 4, 7, 12, 5, 100, 3, 20};
	static int N = arr.length;

	public static void main(String[] args) {
//		quickSort1(0, N-1);
		quickSort2(0, N-1);
		System.out.println(Arrays.toString(arr));
	}

	static void quickSort1(int left, int right) {
		if(left>=right) return;
		int L = left;
		int R = right;
		int pivot = L++;
		while(L<=R) {
			while(L<=R && arr[L]<=arr[pivot]) L++;
			while(arr[R]>arr[pivot]) R--;
			if(L<R) swap(L, R);

		}
		swap(pivot,R);
		quickSort1(pivot, R-1);
		quickSort1(L, right);
	}

	static void quickSort2(int left, int right) {
		if(left>=right) return;
		int pivot = right;
		int i = left-1;
		for(int j = left; j< right; j++) {
			if(arr[j]<arr[pivot]) {
				i++;
				swap(i,j);
			}
		}
		swap(pivot, i+1);

		quickSort1(left, i);
		quickSort1(i+2, right);
	}


	static void swap(int i, int j) {
		int tmp = arr[i];
		arr[i]=arr[j];
		arr[j]=tmp;
	}
}
