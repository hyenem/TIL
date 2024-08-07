import java.util.Arrays;

public class Array2_이진탐색 {
	
	public static void main(String[] args) {
		int[] arr = {2, 4, 7, 9, 11, 19, 23};
		int key =7;
		System.out.println(binarySearch(arr, key));
	}
	
	static int binarySearch(int[] arr,int key) {
		int left = 0; //구간의 시작 index
		int right = arr.length-1; //구간의 끝 index
		while(left<=right) {
			int mid = (left+right)/2;
			if(arr[mid]==key) return mid;
			else if(arr[mid]>key) right = mid-1;
			else left = mid+1;
		}
		return -1;
	}
}
