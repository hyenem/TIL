package SWEA_14229_백만개의정수정렬;

import java.util.Scanner;

public class Solution {
	
	static int[] arr;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		arr = new int[1000000];
		for(int i = 0; i<arr.length; i++) {
			arr[i]=sc.nextInt();
		}
		
		quickSort(0, arr.length-1);
		System.out.println(arr[500000]);
	}
	
	static void quickSort(int left, int right) {
		if(left>500000) return;
		int pivot = right;
		int i = left-1;
		for(int j = left; j<right; j++) {
			if(arr[j]<arr[pivot]) {
				i++;
				swap(i, j);
			}
		}
		swap(i+1, pivot);
		if(left<i) quickSort(left, i);
		if(i+2<right) quickSort(i+2, right);
	}
	
	static void swap(int i, int j) {
		int tmp = arr[i];
		arr[i]=arr[j];
		arr[j]=tmp;
	}
}
